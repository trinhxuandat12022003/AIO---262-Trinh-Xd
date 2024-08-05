import numpy as np


def compute_mean(X):
    new_x = np.array(X)
    res = np.sum(new_x) / np.size(new_x)
    return res


def compute_std(X):
    mean = compute_mean(X)
    variance = 0
    # your code here *******************
    for i in range(0, len(X)):
        variance += (X[i] - mean) ** 2

    variance = variance / len(X)
    return np.sqrt(variance)


X = [171, 176, 155, 167, 169, 182]
print(compute_std(X))
