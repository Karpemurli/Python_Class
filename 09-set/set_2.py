#unique,immutable

#if we try to insert mutable element into set then it will through error.

# nm={1,2,3,1,2,3,"python"}

# for i in nm:
#     print(i)#unique
    
#immutable
nm={1,2,3,1,2,3,"python",["css",44,55]}

for i in nm:
    print(i)  #TypeError: unhashable type: 'list'
    

    
    
    
    
