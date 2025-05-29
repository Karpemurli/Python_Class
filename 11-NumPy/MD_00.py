

# Creating Multidimensional Arrays

#1 Dimension array

import numpy as ds

from numpy import *

array_1D =ds.array([1,2,3,4,5])

array_2D =array(
    [
        [1,2,3,4],
        [5,6,7,8]
    ]
)

array_3D =ds.array(
    [
        [1,2],
        [3,4],
        [5,6]
    ]
)

# print("1D array: ", array_1D)

# print("2D array: \n", array_2D)

# print("3D array: \n", array_3D)


print("Shape:",array_3D.shape)
print("Num_Dimensions:",array_3D.ndim)
print("Size:",array_3D.size)
print("Data_type:",array_3D.dtype)





