from pathlib import Path
from tensorflow.keras.preprocessing.image import ImageDataGenerator

BASE_DIR = Path(__file__).resolve().parent
DATASET_DIR = BASE_DIR.parent / "dataset" / "archive" / "PlantVillage" / "train"

train_datagen = ImageDataGenerator(rescale=1.0 / 255)
train_generator = train_datagen.flow_from_directory(
    DATASET_DIR,
    target_size=(224, 224),
    batch_size=32,
    class_mode="categorical",
    shuffle=False,
)

class_names = list(train_generator.class_indices.keys())
output_file = BASE_DIR / "class_names.txt"

with open(output_file, "w") as f:
    for name in class_names:
        f.write(name + "\n")

print("\n========== CLASS NAMES ==========")
for i, name in enumerate(class_names):
    print(f"{i}: {name}")
print(f"\n✅ Class names saved to:\n{output_file}")
