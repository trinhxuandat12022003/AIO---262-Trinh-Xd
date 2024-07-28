import numpy as np


def compute_vector_length(vector):
    len_of_vector = np.linalg.norm(vector)
    return len_of_vector


vector = np. array([3, 4])
result = compute_vector_length([vector])
print(round(result, 2))
