# Mathematical properties

from numpy import*
import numpy as mk

# demo=array([10,30,50,70,50,50,90],int)
demo=mk.array([10,30,50,70,50,50,90],int)



#Arithmetic operations


def opration():
    print("Original array=",demo)
    print("The addition is=",demo+5)
    print("The subtraction is=",demo-10)
    print("Multiplying is=",demo*2)
    print("Dividing is=",demo/2)
    print("Square root=",mk.sqrt(demo))
    print("Power of 2=",mk.power(demo,2))
    
    
    
    
    
    
opration()