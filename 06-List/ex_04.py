# write a python program to remove duplicates from a list.


lst=[11,12,13,14,15,16,17,18,19,20,11,12,13]
print("list 1 is  ",lst)
lst2=[]


for i in lst:
    if i not in lst2:
        lst2.append(i)   #adding element to end of list
print("THe list 2 is",lst2)