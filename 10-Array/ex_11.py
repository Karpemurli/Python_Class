# Write a Python program that removes all duplicate elements from an array and returns a new array.
# Sample Output:
# Original array: 1 3 5 1 3 7 9
# After removing duplicate elements from the said array: 1 3 5 7 9

from array import *

original_array = array('i', [1, 3, 5, 1, 3, 7, 9])

print("Original array:", original_array)

unique_array = array('i',list(set(original_array)))

print("After removing duplicate elements from the said array:", unique_array)

