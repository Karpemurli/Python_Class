#this is the example of multi dimensional array

import numpy as sd
from numpy import *

# 3 X 3 = 9

my=sd.array(
    [
        ['a','b','c'],
        ['d','e','f'],
        ['g','h','i']
    ]
)

# print(my)
# print("Element at[0,1]=",my[0,1])#b
# print('Row1=',my[0,:])#Row1= ['a' 'b' 'c']

# print('Row1=',my[:,0])#Row1= ['a' 'd' 'g']

# print("Col1=",my[0:2,0:3])


for i in range(my.shape[0]):
    for j in range(my.shape[1]):
        print(f"Element at[{i},{j}] is {my[i,j]}")