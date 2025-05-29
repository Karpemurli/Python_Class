# Write a Python program to create an array of 5 integers and display the array items. Access individual elements through indexes.


from array import*

demo=array('i',[10,20,30,40,50])

for i in range(len(demo)):
    print("Element index ",i,"=",demo[i])
    
    
# check_the_element_=30
# index=demo.index(check_the_element_)

# print("element",check_the_element_,"is at index",index)