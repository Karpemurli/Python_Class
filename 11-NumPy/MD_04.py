# user input in multidimensional array

from numpy import *
import numpy as ss 


rows=int(input("Enter the number of rows="))

colums=int(input("Enter the number of columns="))

myArr=ss.zeros((rows,colums),dtype=int)

print("Enter the element row by row")
for i in range(rows):
    for j in range(colums):
        myArr[i,j] =int(input(f"Element at [{i},{j}]="))
print("\n 2D array is as below")
print(myArr)


