'''
Function for question 5
'''
import math
def calc_elu ( x ) :
  if x <= 0:
    return 0.01 * (math.exp(x) - 1)
  else:
    return x

assert round ( calc_elu (1) ) ==1
print ( round ( calc_elu ( -1) , 2) )