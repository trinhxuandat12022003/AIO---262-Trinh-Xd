import numpy as np


def inverse_matrix(matrix):
    result = np.linalg.inv(matrix)
    return result


m1 = np. array ([[ -2 , 6] , [8 , -4]])
result = inverse_matrix (m1)
print ( result )
