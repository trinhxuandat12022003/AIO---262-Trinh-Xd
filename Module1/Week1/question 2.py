'''
Function for question 2
'''
import math


def is_number(n):
    try:
        int(n)
        return 1.0
    except ValueError:
        return 0.0


assert is_number(3) == 1.0
assert is_number('-2a') == 0.0
print(is_number(1))
print(is_number('n'))
