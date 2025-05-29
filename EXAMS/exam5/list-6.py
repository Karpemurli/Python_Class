# 6.	Write a program to merge two lists without using the + operator.



def mergelist(list1,list2):
    
    for i in list2:
        list1.append(i)
        
    return list1

list1 = [1, 2, 3]
list2 = [4,5,6,7,8,9,10]

merge=mergelist(list1,list2)


print(f'Merging list :',merge)
        