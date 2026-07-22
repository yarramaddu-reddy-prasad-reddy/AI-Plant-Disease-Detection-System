from pathlib import Path
from tensorflow.keras.models import load_model

BASE_DIR = Path(__file__).resolve().parent.parent

MODEL_PATH = BASE_DIR / "ml_model" / "plant_disease_model.keras"

model = None


def load_ai_model():
    global model

    if model is None:
        print("=" * 50)
        print("Loading Plant Disease AI Model...")
        print(f"Model Path: {MODEL_PATH}")

        model = load_model(MODEL_PATH)

        print("✅ AI Model Loaded Successfully")
        print("=" * 50)

    return model