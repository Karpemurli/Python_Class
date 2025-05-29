
#user input
import array as ss
from array import*


myarray =array('i',[])

how_many_elements =int(input("enter how many elements="))

for i in range(0,how_many_elements):
    myarray.append(int(input("Enter the element=")))
    
print("The array elements are below:")
for j in myarray:
    print(j)