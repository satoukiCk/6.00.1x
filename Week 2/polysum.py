from math import *
def polysum(n,s):
    area = 0.25*n*s*s/tan(pi/n)
    parimeter = n*s
    sum = area + parimeter**2
    sum = round(sum,4)
    return sum
