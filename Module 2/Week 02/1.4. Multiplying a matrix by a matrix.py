import numpy as np


def matrix_multi_matrix(matrix1, matrix2):
    len_of_vector = np.dot(matrix1, matrix2)
    return len_of_vector


m1 = np. array([[1, 2], [3, 4]])
m1 = np. reshape(m1, (-1, 4), "F")[0]
m2 = np. array([[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3], [4, 4, 4, 4]])
result = m1@m2
print(result)
