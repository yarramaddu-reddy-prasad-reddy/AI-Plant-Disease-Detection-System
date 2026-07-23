from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

from database.db import get_connection

dashboard_bp = Blueprint("dashboard", __name__)


@dashboard_bp.route("/dashboard", methods=["GET"])
@jwt_required()
def dashboard():

    user_id = int(get_jwt_identity())

    print("\n" + "=" * 60)
    print("LOGGED USER ID :", user_id)
    print("=" * 60)

    conn = get_connection()
    cursor = conn.cursor()

    try:
        # ===================================
        # Total Predictions
        # ===================================
        cursor.execute("""
            SELECT COUNT(*)
            FROM prediction_history
            WHERE user_id = %s
        """, (user_id,))

        total_predictions = cursor.fetchone()[0] or 0
        print("Total Predictions :", total_predictions)

        # ===================================
        # Healthy Plants
        # ===================================
        # Since there is NO status column,
        # we identify healthy predictions
        # from disease_name.
        cursor.execute("""
            SELECT COUNT(*)
            FROM prediction_history
            WHERE user_id = %s
            AND LOWER(disease_name) LIKE %s
        """, (user_id, "%healthy%"))

        healthy = cursor.fetchone()[0] or 0
        print("Healthy Plants :", healthy)

        # ===================================
        # Diseased Plants
        # ===================================
        diseased = total_predictions - healthy
        print("Diseased Plants :", diseased)

        # ===================================
        # Average Confidence
        # ===================================
        cursor.execute("""
            SELECT AVG(confidence)
            FROM prediction_history
            WHERE user_id = %s
        """, (user_id,))

        avg = cursor.fetchone()[0]

        accuracy = round(float(avg), 2) if avg else 0

        print("Average Confidence :", accuracy)
        print("=" * 60)

        return jsonify({
            "total_predictions": total_predictions,
            "healthy_plants": healthy,
            "diseased_plants": diseased,
            "accuracy": accuracy
        }), 200
    except Exception as error:
        conn.rollback()
        return jsonify({
            "error": "Failed to load dashboard data",
            "details": str(error)
        }), 500
    finally:
        cursor.close()
        conn.close()