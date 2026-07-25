from pathlib import Path
import tensorflow as tf

BASE_DIR = Path(__file__).resolve().parent.parent

MODEL_PATH = BASE_DIR / "ml_model" / "plant_disease_model.tflite"

model = None


def load_ai_model():
    global model

    if model is None:
        print("=" * 50)
        print("Loading Plant Disease TFLite Model...")
        print(f"Model Path: {MODEL_PATH}")

        model = tf.lite.Interpreter(model_path=str(MODEL_PATH))
        model.allocate_tensors()

        print("✅ TFLite Model Loaded Successfully")
        print("=" * 50)

    return model
