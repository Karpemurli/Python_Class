# 4.Write a Python program to get the number of occurrences of a specified element in an array.
# Sample Output:
# Original array: array('i', [1, 3, 5, 3, 7, 9, 3])
# Number of occurrences of the number 3 in the said array: 3


from array import *


mydemo=array('i',[1,2,3,1,1,67,7,8])

print("Original array: ",mydemo)

# element=1
element=int(input("enter the element:"))

occurrences=mydemo.count(element)

print(f"Number of occurrences {element} = ",occurrences)