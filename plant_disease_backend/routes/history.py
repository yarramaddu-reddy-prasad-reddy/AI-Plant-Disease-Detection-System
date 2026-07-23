from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from psycopg2.extras import RealDictCursor

from database.db import get_connection
from utils.disease_info import DISEASE_INFO

history_bp = Blueprint("history", __name__)

@history_bp.route("/history", methods=["GET"])
@jwt_required()
def get_user_history():
    user_id = get_jwt_identity()

    conn = get_connection()
    cursor = conn.cursor(cursor_factory=RealDictCursor)

    cursor.execute(
        """
        SELECT 
            prediction_id,
            image_path,
            plant_name,
            disease_name,
            confidence,
            prediction_time
        FROM prediction_history
        WHERE user_id = %s
        ORDER BY prediction_time DESC
        """,
        (user_id,)
    )

    records = cursor.fetchall()
    cursor.close()
    conn.close()

    formatted_history = []
    for item in records:
        # Reconstruct plant class string to lookup details
        formatted_plant = item["plant_name"].replace(" ", "_")
        formatted_disease = item["disease_name"].replace(" ", "_")
        lookup_key = f"{formatted_plant}___{formatted_disease}"

        # Determine health status
        status = "Healthy" if item["disease_name"].lower() == "healthy" else "Diseased"

        # Build full image HTTP URL
        filename = item["image_path"].replace("\\", "/").split("/")[-1]
        image_url = f"{request.host_url.rstrip('/')}/uploads/{filename}"

        formatted_history.append({
            "prediction_id": item["prediction_id"],
            "plant_name": item["plant_name"],
            "disease_name": item["disease_name"],
            "status": status,
            "confidence": float(item["confidence"]),
            "prediction_time": item["prediction_time"].isoformat() if item["prediction_time"] else None,
            "image_url": image_url,
            "details": DISEASE_INFO.get(lookup_key, {})
        })

    return jsonify(formatted_history), 200


@history_bp.route("/history/<int:prediction_id>", methods=["DELETE"])
@jwt_required()
def delete_history_item(prediction_id):
    user_id = get_jwt_identity()

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM prediction_history WHERE prediction_id = %s AND user_id = %s",
        (prediction_id, user_id)
    )
    conn.commit()
    rows_affected = cursor.rowcount

    cursor.close()
    conn.close()

    if rows_affected == 0:
        return jsonify({"error": "Record not found or unauthorized"}), 404

    return jsonify({"message": "Record deleted successfully"}), 200