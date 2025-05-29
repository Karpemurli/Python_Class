# Write a Python program to check if two given sets have no elements in common
set1=set(['a', 'b', 'c'] )

set2=set([ 'd', 'e', 'f', 'g'])


if set1.isdisjoint(set2):
    print('No common elements')
else:
    print('Common elements:', set1 & set2)