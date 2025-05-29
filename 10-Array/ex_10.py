# Write a Python program to find the missing number in a given array of numbers between 10 and 20.
# Sample Output:
# Original array: 10 11 12 13 14 16 17 18 19 20
# Missing number in the said array (10-20): 15

import array as ss 
# from array import *

original_array= ss.array('i',[10,11,12,13,16,17,18,20])

complet_set=set(range(10,21))

missing_numbers=complet_set-set(original_array)

print("Original array: ",original_array)
print("Missing numbers: ",missing_numbers)



# array = [10,11,12, 13, 14, 16, 17, 19, 20]
# my_set = set(range(10,21))
# array_set = set(array)
# missing_num = my_set - array_set
# missing_num = sorted(missing_num)
# print("The missing number is = ",missing_num)