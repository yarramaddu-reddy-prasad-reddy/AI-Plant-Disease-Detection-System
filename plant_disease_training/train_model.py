import os
from pathlib import Path

from tensorflow.keras import layers, models
from tensorflow.keras.preprocessing.image import ImageDataGenerator

BASE_DIR = Path(__file__).resolve().parent
DATASET_DIR = BASE_DIR.parent / "dataset" / "archive" / "PlantVillage" / "train"
MODEL_DIR = BASE_DIR / "models"
MODEL_PATH = MODEL_DIR / "plant_disease_model.keras"

img_height = 224
img_width = 224
batch_size = 32
epochs = 5

if not DATASET_DIR.exists():
    raise FileNotFoundError(f"Dataset directory not found: {DATASET_DIR}")

train_datagen = ImageDataGenerator(
    rescale=1.0 / 255,
    validation_split=0.2,
)

train_generator = train_datagen.flow_from_directory(
    DATASET_DIR,
    target_size=(img_height, img_width),
    batch_size=batch_size,
    class_mode="categorical",
    subset="training",
)

validation_generator = train_datagen.flow_from_directory(
    DATASET_DIR,
    target_size=(img_height, img_width),
    batch_size=batch_size,
    class_mode="categorical",
    subset="validation",
)

num_classes = len(train_generator.class_indices)

model = models.Sequential([
    layers.Input(shape=(img_height, img_width, 3)),
    layers.Conv2D(32, (3, 3), activation="relu"),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(64, (3, 3), activation="relu"),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(128, (3, 3), activation="relu"),
    layers.MaxPooling2D((2, 2)),
    layers.Flatten(),
    layers.Dense(128, activation="relu"),
    layers.Dropout(0.3),
    layers.Dense(num_classes, activation="softmax"),
])

model.compile(
    optimizer="adam",
    loss="categorical_crossentropy",
    metrics=["accuracy"],
)

model.fit(
    train_generator,
    validation_data=validation_generator,
    epochs=epochs,
)

MODEL_DIR.mkdir(parents=True, exist_ok=True)
model.save(MODEL_PATH)
print(f"Model saved to {MODEL_PATH}")
