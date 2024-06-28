'''
Function for question 10
'''
import math


def approx_sin(x, n):
    res = 0
    for i in range(0, n+1):
        res += (-1)**i * x**(2 * i + 1)/math.factorial(2 * i + 1)
    return res


assert round(approx_sin(x=1, n=10), 4) == 0.8415
print(round(approx_sin(x=3.14, n=10), 4))
