# 3.	Write a program to remove duplicate elements from a list while maintaining order.


def remove_duplicates(list):
    
    
    set1=set()
    unique_list=[]
    
    
    for i in list:
        if i not in set1:
            unique_list.append(i)
            set1.add(i)
    return unique_list

list=[1,2,3,4,5,'mk','sk','mk']

duplicates=remove_duplicates(list)

print(f'Duplicates : ',duplicates) 
            