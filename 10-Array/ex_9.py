# Write a Python program to find the first duplicate element in a given array of integers. Return -1 if there are no such elements.
# Sample Output:
# 4
# -1
# 1

from array import array

# arr=array('i',([1, 2, 3, 4, 4, 5]))
arr=array('i',([1, 2, 3,4]))
# arr=array('i',[1,2,3,1,4,5])

demo=set()

for i in arr:
    if i in demo:
        print(i)
        break
    else:
        demo.add(i)
        


