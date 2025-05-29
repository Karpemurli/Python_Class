# 8.	Write a Python program to find the intersection (common elements) of two lists.



def list_intersect(lst1, lst2):
    
   return list(set(lst1) & set(lst2))

        

lst1=[1,2,3,4,5,'apple','orange']
lst2=[3,4,5,'apple']

intersection=list_intersect(lst1, lst2)

print(f'Intersection : ',intersection)  
