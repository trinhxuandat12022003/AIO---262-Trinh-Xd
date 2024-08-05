import numpy as np
import math


def calculate_denominator(x):
    N = len(x)
    denom = 0
    for i in range(0, N):
        denom += x[i] ** 2
    denom = N * denom
    denom = denom - sum(x) ** 2
    denom = math.sqrt(denom)
    return denom


def compute_correlation_cofficient(X, Y):
    N = len(X)
    numerator = 0
    denominator = 0
    # your code here ****************
    for i in range(0, N):
        numerator += X[i] * Y[i]
    numerator = N * numerator
    numerator = numerator - np.sum(X) * np.sum(Y)
    denominator = calculate_denominator(X) * calculate_denominator(Y)
    return np.round(numerator/denominator, 2)


X = np.asarray([-2, -5, -11, 6, 4, 15, 9])
Y = np.asarray([4, 25, 121, 36, 16, 225, 81])
print("Correlation : ", compute_correlation_cofficient(X, Y))
