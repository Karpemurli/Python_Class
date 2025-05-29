# Relational Operators



import numpy as fn

arr=fn.array([10,30,50],dtype=int)
arr2=fn.array([20,40,60],int)
arr3=fn.array([10,30,50],int)

def test():
    print("Greater than=",arr > arr2)
    print("Less than=",arr < arr2)
    print("Equal =",fn.array_equal(arr,arr3))  #array_equal method
    print("Equal =",arr2 == arr3)
    print("Not equal =",arr!= arr2)
    

    
    


test()