# 9.	Write a Python program to find unique elements in a NumPy array.
import numpy as np

arr=np.array([1,1,2,3,4,2,4,5,3,6,8,8,7])

unique_elements=np.unique(arr)

print("Unique elements in the array:",unique_elements)