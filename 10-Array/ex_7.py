# Write a Python program to remove a specified item using the index of an array.
# Sample Output:
# Original array: array('i', [1, 3, 5, 7, 9])
# Remove the third item form the array:
# New array: array('i', [1, 3, 7, 9])

from array import*

original_array = array('i', [1, 3, 5, 7, 9])

print("Original array: ", original_array)

original_array.pop(2)
# index_remove=2
# original_array.pop(index_remove)
print("Original array: ", original_array)