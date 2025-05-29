# Write a Python program to remove a specified item using the index of an array.
# Sample Output:
# Original array: array('i', [1, 3, 5, 7, 9])
# Remove the third item form the array:
# New array: array('i', [1, 3, 7, 9])

import numpy as ss 


original_array=ss.array([1,3,5,7,9])
print("Original array:", original_array)

removed=2

New=ss.delete(original_array,removed)

print("New array:", New)