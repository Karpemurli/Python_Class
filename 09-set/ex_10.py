# Given two sets of numbers, write a Python program to find the missing numbers in the second set as compared to the first and vice versa. Use the Python set.


set1=set([1,2,3,4,5])

set2={3,4,5,6,7}


set3=set1.difference(set2)
set4=set2 - set1

for i in set3,set4:
    print(i)