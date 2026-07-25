import os
import uuid
import numpy as np

from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

from database.db import get_connection
from models.model_loader import load_ai_model
from utils.class_names import CLASS_NAMES
from utils.image_preprocessing import preprocess_image
from utils.confidence import get_confidence_info
from utils.disease_info import DISEASE_INFO

predict_bp = Blueprint("predict", __name__)

# Load AI model once
model = load_ai_model()


def run_tflite_prediction(interpreter, input_data):
    input_details = interpreter.get_input_details()
    output_details = interpreter.get_output_details()

    input_index = input_details[0]["index"]
    output_index = output_details[0]["index"]

    input_dtype = input_details[0]["dtype"]
    input_tensor = input_data.astype(input_dtype)

    interpreter.set_tensor(input_index, input_tensor)
    interpreter.invoke()

    output = interpreter.get_tensor(output_index)
    return output


def allowed_file(filename):
    """
    Check whether uploaded file is a valid image.
    """
    allowed_extensions = {"jpg", "jpeg", "png"}

    return (
        "." in filename
        and filename.rsplit(".", 1)[1].lower() in allowed_extensions
    )


@predict_bp.route("/predict", methods=["POST"])
@jwt_required()
def predict():

    # Check image
    if "image" not in request.files:
        return jsonify({
            "error": "No image uploaded"
        }), 400

    image = request.files["image"]

    if image.filename == "":
        return jsonify({
            "error": "Please select an image"
        }), 400

    if not allowed_file(image.filename):
        return jsonify({
            "error": "Only JPG, JPEG and PNG images are allowed"
        }), 400

    temp_dir = os.path.join(os.getcwd(), "temp_uploads")
    os.makedirs(temp_dir, exist_ok=True)

    # Generate unique filename
    extension = image.filename.rsplit(".", 1)[1].lower()
    filename = f"{uuid.uuid4()}.{extension}"

    image_path = os.path.join(temp_dir, filename)

    # Save image
    image.save(image_path)

    image_url = f"/temp/{filename}"

    # Preprocess image
    processed_image = preprocess_image(image_path)

    # Predict with TFLite interpreter
    prediction = run_tflite_prediction(model, processed_image)

    predicted_index = int(np.argmax(prediction))

    confidence = float(np.max(prediction) * 100)

    # Confidence information
    confidence_info = get_confidence_info(confidence)

    predicted_class = CLASS_NAMES[predicted_index]
    print("=" * 60)
    print("Predicted Class :", predicted_class)
    print("=" * 60)

    # Disease Information
    disease_info = DISEASE_INFO.get(
        predicted_class,
        {
            "description": "No disease information available.",
            "treatment": "Consult a local agricultural expert.",
            "prevention": "Maintain good crop hygiene and monitor plants regularly.",
            "pesticide": "Not Available",
            "organic": "Not Available",
            "watering": "Follow normal watering practices.",
            "fertilizer": "Balanced NPK fertilizer.",
            "severity": "Unknown"
        }
    )

    # Split plant and disease
    plant_name, disease_name = predicted_class.split("___")

    plant_name = (
        plant_name
        .replace("_", " ")
        .replace(",", "")
    )

    disease_name = disease_name.replace("_", " ")

    # Disease Status
    if disease_name.lower() == "healthy":
        status = "Healthy"
    else:
        status = "Diseased"

    # Logged-in User
    user_id = get_jwt_identity()

    # Save Prediction History
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO prediction_history
        (
            user_id,
            image_path,
            plant_name,
            disease_name,
            confidence
        )
        VALUES
        (%s, %s, %s, %s, %s)
        RETURNING prediction_id
        """,
        (
            user_id,
            image_path,
            plant_name,
            disease_name,
            round(confidence, 2)
        )
    )

    prediction_id = cursor.fetchone()[0]
    conn.commit()

    cursor.close()
    conn.close()

    # Response
    return jsonify({

        "message": "Prediction Successful",

        "prediction_id": prediction_id,

        "plant_name": plant_name,

        "disease_name": disease_name,

        "status": status,

        "confidence": round(confidence, 2),

        "confidence_level": confidence_info["level"],

        "confidence_message": confidence_info["message"],

        "description": disease_info["description"],

        "treatment": disease_info["treatment"],

        "prevention": disease_info["prevention"],

        "recommended_pesticide": disease_info["pesticide"],

        "organic_solution": disease_info["organic"],

        "watering_advice": disease_info["watering"],

        "fertilizer_recommendation": disease_info["fertilizer"],

        "disease_severity": disease_info["severity"],

        "image_url": image_url,

        "image_path": image_path

    }), 200