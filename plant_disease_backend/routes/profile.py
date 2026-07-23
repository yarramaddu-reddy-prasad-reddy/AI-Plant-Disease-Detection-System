from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from psycopg2.extras import RealDictCursor
from werkzeug.security import generate_password_hash, check_password_hash
from database.db import get_connection

profile_bp = Blueprint("profile", __name__)

@profile_bp.route("/profile", methods=["GET"])
@jwt_required()
def get_profile():
    user_id = get_jwt_identity()

    conn = get_connection()
    cursor = conn.cursor(cursor_factory=RealDictCursor)

    # Fetch User Info
    cursor.execute(
        """
        SELECT user_id, full_name, email, role, created_at 
        FROM users 
        WHERE user_id = %s
        """,
        (user_id,)
    )
    user = cursor.fetchone()

    if not user:
        cursor.close()
        conn.close()
        return jsonify({"error": "User not found"}), 404

    # Fetch User Prediction Statistics
    cursor.execute(
        """
        SELECT 
            COUNT(*) as total_predictions,
            SUM(CASE WHEN LOWER(disease_name) = 'healthy' THEN 1 ELSE 0 END) as healthy_plants,
            SUM(CASE WHEN LOWER(disease_name) != 'healthy' THEN 1 ELSE 0 END) as diseased_plants,
            AVG(confidence) as avg_confidence
        FROM prediction_history 
        WHERE user_id = %s
        """,
        (user_id,)
    )
    stats = cursor.fetchone()

    cursor.close()
    conn.close()

    total = stats["total_predictions"] or 0
    healthy = stats["healthy_plants"] or 0
    diseased = stats["diseased_plants"] or 0
    avg_accuracy = round(float(stats["avg_confidence"]), 2) if stats["avg_confidence"] else 0.0

    return jsonify({
        "user_id": user["user_id"],
        "full_name": user["full_name"],
        "email": user["email"],
        "role": user.get("role", "Student / Researcher"),
        "created_at": user["created_at"].isoformat() if user["created_at"] else None,
        "total_predictions": total,
        "healthy_plants": healthy,
        "diseased_plants": diseased,
        "accuracy": avg_accuracy
    }), 200


@profile_bp.route("/profile", methods=["PUT"])
@jwt_required()
def update_profile():
    user_id = get_jwt_identity()
    data = request.get_json()

    full_name = data.get("full_name")
    email = data.get("email")

    if not full_name or not email:
        return jsonify({"error": "Full Name and Email are required"}), 400

    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute(
            """
            UPDATE users 
            SET full_name = %s, email = %s 
            WHERE user_id = %s
            """,
            (full_name, email, user_id)
        )
        conn.commit()
        return jsonify({"message": "Profile updated successfully"}), 200
    except Exception as e:
        conn.rollback()
        return jsonify({"error": "Email already exists or database error"}), 400
    finally:
        cursor.close()
        conn.close()


@profile_bp.route("/change-password", methods=["PUT"])
@jwt_required()
def change_password():
    user_id = get_jwt_identity()
    data = request.get_json()

    current_password = data.get("current_password")
    new_password = data.get("new_password")

    if not current_password or not new_password:
        return jsonify({"error": "Both current and new passwords are required"}), 400

    conn = get_connection()
    cursor = conn.cursor(cursor_factory=RealDictCursor)

    cursor.execute("SELECT password_hash FROM users WHERE user_id = %s", (user_id,))
    user = cursor.fetchone()

    if not user or not check_password_hash(user["password_hash"], current_password):
        cursor.close()
        conn.close()
        return jsonify({"error": "Incorrect current password"}), 400

    new_hash = generate_password_hash(new_password)
    cursor.execute(
        "UPDATE users SET password_hash = %s WHERE user_id = %s",
        (new_hash, user_id)
    )
    conn.commit()

    cursor.close()
    conn.close()

    return jsonify({"message": "Password changed successfully"}), 200