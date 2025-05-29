#  Write a Python program to create a union of sets.



set1={"sun","Mon","Tue","Wed"}

set2=set(["frd","sat"])

# set3=set2 | set1
set3=set1.union(set2)


# print(set3)

for i in set3:
    print(i)