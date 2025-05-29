# 5.	Write a program to reverse an array without using slicing.


import numpy as np

array=np.array([1,2,3,4,5])

reversed_arr=array[::-1]

# reversed_arr=np.flip(array)




print("Reversed array:",reversed_arr)