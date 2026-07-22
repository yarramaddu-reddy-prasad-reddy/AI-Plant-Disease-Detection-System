from pathlib import Path

import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

from classes import CLASS_NAMES

BASE_DIR = Path(__file__).resolve().parent
MODEL_PATH = BASE_DIR / "models" / "plant_disease_model.keras"

if not MODEL_PATH.exists():
    raise FileNotFoundError(f"Trained model not found at {MODEL_PATH}")

model = load_model(MODEL_PATH)


def predict_image(image_path: str):
    img = image.load_img(image_path, target_size=(224, 224))
    img_array = image.img_to_array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    prediction = model.predict(img_array, verbose=0)[0]
    class_index = int(np.argmax(prediction))
    confidence = float(prediction[class_index])

    return {
        "class_name": CLASS_NAMES[class_index],
        "confidence": confidence,
    }


if __name__ == "__main__":
    sample_path = input("Enter image path: ").strip()
    print(predict_image(sample_path))
