# 6.	How can you reshape a 1D array into a 2D array using NumPy?
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6])


reshape=arr.reshape(2,3) #row 2,row 3

print(f'Reshaped 2d array: \n',reshape)
