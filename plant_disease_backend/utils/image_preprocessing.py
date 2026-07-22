from PIL import Image
import numpy as np

# Image size used during model training
IMG_SIZE = (224, 224)


def preprocess_image(image_path):
    """
    Load an image and preprocess it for the TensorFlow model.
    Returns a NumPy array with shape (1, 224, 224, 3).
    """

    # Open image
    img = Image.open(image_path).convert("RGB")

    # Resize to model input size
    img = img.resize(IMG_SIZE)

    # Convert to NumPy array
    img_array = np.array(img, dtype=np.float32)

    # Normalize pixel values (0-255 -> 0-1)
    img_array = img_array / 255.0

    # Add batch dimension
    img_array = np.expand_dims(img_array, axis=0)

    return img_array