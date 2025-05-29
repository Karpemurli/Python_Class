
# 9.	How can you find the union of two lists without duplicates?


def list_union(lst1, lst2):
    
    
    return list(set(lst1) | set(lst2))
#    return list(set(lst1).union(set(lst2)))



        

lst1=[1,2,3,4]
lst2=[4,5,'apple']

Union=list_union(lst1, lst2)

print(f'Union : ',Union)  