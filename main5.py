"""
This is free and unencumbered software released into the public domain.

Anyone is free to copy, modify, publish, use, compile, sell, or
distribute this software, either in source code form or as a compiled
binary, for any purpose, commercial or non-commercial, and by any
means.

In jurisdictions that recognize copyright laws, the author or authors
of this software dedicate any and all copyright interest in the
software to the public domain. We make this dedication for the benefit
of the public at large and to the detriment of our heirs and
successors. We intend this is free and unencumbered software released into the public domain.

Anyone is free to copy, modify, publish, use, compile, sell, or
distribute this software, either in source code form or as a compiled
binary, for any purpose, commercial or non-commercial, and by any
means.

In jurisdictions that recognize copyright laws, the author or authors
of this software dedicate any and all copyright interest in the
software to the public domain. We make this dedication for the benefit
of the public at large and to the detriment of our heirs and
successors. We intend this dedication to be an overt act of
relinquishment in perpetuity of all present and future rights to this
software under copyright law.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
OTHER DEALINGS IN THE SOFTWARE.

For more information, please refer to <https://unlicense.org>
"""
import os
from tensorflow.keras.applications.mobilenet_v2 import MobileNetV2, preprocess_input, decode_predictions
from tensorflow.keras.preprocessing import image
import numpy as np

# Path to the PetImages directory
DATASET_PATH = "kagglecatsanddogs_5340/PetImages"

# Model name
MODEL = "mobilenet_v2"


def load_and_preprocess_image(image_path: str) -> np.ndarray:
    """Load and preprocess an image for the model.

    Args:
        image_path (str): Path to the image file.

    Returns:
        np.ndarray: Preprocessed image as a NumPy array.
    """
    try:
        # Load the image and resize it to (224, 224)
        img = image.load_img(image_path, target_size=(224, 224))
        img_array = image.img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0)
        img_array = preprocess_input(img_array)
        return img_array
    except Exception as e:
        print(f"Error loading image {image_path}: {e}")
        return None


def classify_image(model, image_path: str) -> None:
    """Classify an image using the pre-trained model.

    Args:
        model: The pre-trained model.
        image_path (str): Path to the image file.
    """
    img_array = load_and_preprocess_image(image_path)
    if img_array is not None:
        # Make predictions
        predictions = model.predict(img_array)
        decoded_predictions = decode_predictions(predictions, top=3)[0]

        # Print the top 3 predictions
        print(f"Image: {image_path}")
        print(f"{MODEL} response:")
        for i, (imagenet_id, label, score) in enumerate(decoded_predictions):
            print(f"{i + 1}: {label} ({score:.2f})")
        print("-" * 50)


def process_directory(model, directory: str) -> None:
    """Recursively process all images in a directory.

    Args:
        model: The pre-trained model.
        directory (str): Path to the directory containing images.
    """
    for root, _, files in os.walk(directory):
        for file in files:
            if file.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
                image_path = os.path.join(root, file)
                classify_image(model, image_path)


def main() -> None:
    # Load the pre-trained MobileNetV2 model
    model = MobileNetV2(weights="imagenet")

    # Process the Cat directory
    cat_directory = os.path.join(DATASET_PATH, "Cat")
    print(f"Processing images in {cat_directory}...")
    process_directory(model, cat_directory)

    # Process the Dog directory
    dog_directory = os.path.join(DATASET_PATH, "Dog")
    print(f"Processing images in {dog_directory}...")
    process_directory(model, dog_directory)

if __name__ == "__main__":
    main()
