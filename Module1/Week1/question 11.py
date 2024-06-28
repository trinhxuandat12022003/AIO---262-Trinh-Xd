'''
Function for question 11
'''
import math


def approx_sinh(x, n):
    res = 0
    for i in range(0, n+1):
        res += x**(2 * i + 1)/math.factorial(2 * i + 1)
    return res


assert round(approx_sinh(x=1, n=10), 2) == 1.18
print(round(approx_sinh(x=3.14, n=10), 2))
