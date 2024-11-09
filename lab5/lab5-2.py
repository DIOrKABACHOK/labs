import numpy as np
from PIL import Image

image = Image.open('wc.png')

image_array = np.array(image)

weights = np.array([0.299, 0.587, 0.114])

gray_image = np.dot(image_array, weights)

print("Исходное изображение:")
print(image_array)
print("\nПреобразованное изображение в оттенки серого:")
print(gray_image)