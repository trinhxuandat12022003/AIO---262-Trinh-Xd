'''
Function for question 9
'''
import math


def approx_cos(x, n):
    res = 0
    for i in range(0, n+1):
        res += (-1)**i * x**(2 * i)/math.factorial(2 * i)
    return res


assert round(approx_cos(x=1, n=10), 2) == 0.54
print(round(approx_cos(x=3.14, n=10), 2))
