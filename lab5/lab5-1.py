import numpy as np

# 1. Создайте вектор с элементами от 12 до 42
vector_1 = np.arange(12, 43)
print("1. Вектор с элементами от 12 до 42:")
print(vector_1)

# 2. Создайте вектор из нулей длины 12, но его пятый элемент должен быть равен 1
vector_2 = np.zeros(12)
vector_2[4] = 1
print("\n2. Вектор из нулей длины 12, пятый элемент равен 1:")
print(vector_2)

# 3. Создайте матрицу (3, 3), заполненную от 0 до 8
matrix_3 = np.arange(9).reshape(3, 3)
print("\n3. Матрица (3, 3), заполненная от 0 до 8:")
print(matrix_3)

# 4. Найдите все положительные числа в np.array([1,2,0,0,4,0])
positive_numbers = np.array([1, 2, 0, 0, 4, 0])[np.array([1, 2, 0, 0, 4, 0]) > 0]
print("\n4. Положительные числа в массиве [1, 2, 0, 0, 4, 0]:")
print(positive_numbers)

# 5. Умножьте матрицу размерности (5, 3) на (3, 2)
matrix_5_3 = np.random.rand(5, 3)
matrix_3_2 = np.random.rand(3, 2)
result_matrix = np.dot(matrix_5_3, matrix_3_2)
print("\n5. Умножение матрицы (5, 3) на (3, 2):")
print(result_matrix)

# 6. Создайте матрицу (10, 10) так, чтобы на границе были 0, а внутри 1
matrix_6 = np.ones((10, 10))
matrix_6[0, :] = 0
matrix_6[-1, :] = 0
matrix_6[:, 0] = 0
matrix_6[:, -1] = 0
print("\n6. Матрица (10, 10) с границами 0 и внутренностью 1:")
print(matrix_6)

# 7. Создайте рандомный вектор и отсортируйте его
random_vector = np.random.rand(10)
sorted_vector = np.sort(random_vector)
print("\n7. Рандомный вектор и его отсортированная версия:")
print("Исходный вектор:", random_vector)
print("Отсортированный вектор:", sorted_vector)

# 8. Каков эквивалент функции enumerate для numpy массивов?
# Эквивалент функции enumerate для numpy массивов - это функция np.ndenumerate
print("\n8. Эквивалент функции enumerate для numpy массивов: np.ndenumerate")

# 9. Создайте рандомный вектор и выполните нормализацию столбцов
random_matrix = np.random.rand(5, 3)
normalized_matrix = (random_matrix - np.mean(random_matrix, axis=0)) / np.std(random_matrix, axis=0)
print("\n9. Рандомный вектор и его нормализованная версия:")
print("Исходная матрица:")
print(random_matrix)
print("Нормализованная матрица:")
print(normalized_matrix)

# 10. Для заданного числа найдите ближайший к нему элемент в векторе
given_number = 3.5
vector_10 = np.array([1, 2, 3, 4, 5])
closest_element = vector_10[np.argmin(np.abs(vector_10 - given_number))]
print("\n10. Ближайший элемент к числу 3.5 в векторе [1, 2, 3, 4, 5]:")
print(closest_element)

# 11. Найдите N наибольших значений в векторе
N = 3
vector_11 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
largest_values = np.partition(vector_11, -N)[-N:]
print("\n11. Три наибольших значения в векторе [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:")
print(largest_values)