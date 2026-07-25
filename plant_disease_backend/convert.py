import tensorflow as tf
import os

# Path to your Keras model
keras_model_path = r"ml_model\plant_disease_model.keras"

# Output path for TFLite model
tflite_model_path = r"ml_model\plant_disease_model.tflite"

# Load the Keras model
model = tf.keras.models.load_model(keras_model_path)

# Create the converter
converter = tf.lite.TFLiteConverter.from_keras_model(model)

# Convert the model
tflite_model = converter.convert()

# Save the TFLite model
with open(tflite_model_path, "wb") as f:
    f.write(tflite_model)

print("✅ Conversion completed!")
print(f"TFLite model saved at: {os.path.abspath(tflite_model_path)}")
print(f"Size: {os.path.getsize(tflite_model_path) / (1024 * 1024):.2f} MB")