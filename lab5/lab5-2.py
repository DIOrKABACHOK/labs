import numpy as np
from PIL import Image

image = Image.open('wc.png')

image_array = np.array(image)

weights = np.array([0.299, 0.587, 0.114])

gray_image = np.dot(image_array, weights)

gray_image_uint8 = gray_image.astype(np.uint8)

gray_image_pil = Image.fromarray(gray_image_uint8)

gray_image_pil.save('gray_image.png')

print("Исходное изображение:")
print(image_array)
print("\nПреобразованное изображение в оттенки серого:")
print(gray_image)
print("\nИзображение сохранено как 'gray_image.png'")
