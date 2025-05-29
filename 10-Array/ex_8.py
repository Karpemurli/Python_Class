# Write a Python program to remove the first occurrence of a specified element from an array.
# Sample Output:
# Original array: array('i', [1, 3, 5, 3, 7, 1, 9, 3])
# Remove the first occurrence of 3 from the said array:
# New array: array('i', [1, 5, 3, 7, 1, 9, 3])

from array import*

original_array = array('i', [1, 3, 5, 3, 7, 1, 9, 3])

print("Original array:", original_array)

# original_array.remove(3)
# print("Removed array:", original_array)

element_to_remove=int(input('Enter the element to remove='))

if element_to_remove in original_array:
    original_array.remove(element_to_remove)
    print("New array:",original_array)
else:
    print("element not found.{element_to_remove}")

