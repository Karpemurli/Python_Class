#  Write a Python program to find elements in a given set that are not in another set.


set1=set(['a', 'b', 'c'])
set2=set(['a', 'b', 'd','e'])

set3=set1.difference(set2)

for i in set3:
    print(i)

