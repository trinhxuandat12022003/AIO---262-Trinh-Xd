'''
Function for question 12
'''
import math


def approx_cosh(x, n):
    res = 0
    for i in range(0, n+1):
        res += x**(2 * i)/math.factorial(2 * i)
    return res


assert round(approx_cosh(x=1, n=10), 2) == 1.54
print(round(approx_cosh(x=3.14, n=10), 2))
