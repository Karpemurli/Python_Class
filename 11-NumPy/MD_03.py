
from numpy import *

import numpy as mk

my= array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])

# print(my)

#Access elements using indices or slices:

# print(my[0,0])#1
# print(my[0,1])#2
# print(my[0,2])#3

# print(my[2,1])#8

# print(my[1,2])#6

#slice elements
# print(my[:,1])

print(my[1:,1])

print(my[1,:1])