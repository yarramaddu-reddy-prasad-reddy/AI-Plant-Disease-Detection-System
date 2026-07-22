from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

from database.db import get_connection

dashboard_bp = Blueprint("dashboard", __name__)


@dashboard_bp.route("/dashboard", methods=["GET"])
@jwt_required()
def dashboard():

    user_id = get_jwt_identity()

    conn = get_connection()
    cursor = conn.cursor()

    # Total Predictions
    cursor.execute(
        """
        SELECT COUNT(*)
        FROM prediction_history
        WHERE user_id=%s
        """,
        (user_id,)
    )

    total_predictions = cursor.fetchone()[0]

    # Healthy Plants
    cursor.execute(
        """
        SELECT COUNT(*)
        FROM prediction_history
        WHERE user_id=%s
        AND disease_name='Healthy'
        """,
        (user_id,)
    )

    healthy = cursor.fetchone()[0]

    diseased = total_predictions - healthy

    # Average Confidence
    cursor.execute(
        """
        SELECT AVG(confidence)
        FROM prediction_history
        WHERE user_id=%s
        """,
        (user_id,)
    )

    avg = cursor.fetchone()[0]

    accuracy = round(avg,2) if avg else 0

    cursor.close()
    conn.close()

    return jsonify({

        "total_predictions":total_predictions,

        "healthy_plants":healthy,

        "diseased_plants":diseased,

        "accuracy":accuracy

    }),200