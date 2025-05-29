# 7.	Write a program to concatenate two NumPy arrays.
import numpy as np


array1=np.array(
    [1,2,3,4,5]
    
)

array2= np.array(
    ['a','b','c','d','e']
)

concatenate_arrays=np.concatenate((array1,array2))

print("Concatenated arrays:",concatenate_arrays)