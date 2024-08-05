import numpy as np


def compute_mean(X):
    new_x = np.array(X)
    res = np.sum(new_x) / np.size(new_x)
    return res


X = [2, 0, 2, 2, 7, 4, -2, 5, -1, -1]

print("Mean :", compute_mean(X))
