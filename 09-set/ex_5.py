
#  Write a Python program to create set difference.

set1={"Goldline","Eest","MV9","DhDAM"}

set2=set({"UE Company","Nexa Cobinet","RP Cabinet","Eest","Goldline",})

# print(set1.difference(set2))

set3=set2 - set1

for i in set3:
    print(i)