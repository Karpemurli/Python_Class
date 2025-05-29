
import array as mk  
# from array import*

myarray=mk.array('u',['a','b','c','d','e','f','g','h','i','j','k'])


for i in range(len(myarray)):
    print(i,myarray[i])
    
element_to_check='h'
index=myarray.index(element_to_check)
print("element",element_to_check,"is at index",index)




