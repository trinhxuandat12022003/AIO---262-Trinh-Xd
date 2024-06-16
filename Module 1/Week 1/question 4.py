'''
Function for question 4
'''
import math


def calc_sig(x):
    return 1 / (1 + math.exp(-x))


assert round(calc_sig(3), 2) == 0.95
print(round(calc_sig(2), 2))
