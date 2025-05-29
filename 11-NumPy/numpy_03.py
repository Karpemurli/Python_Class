

#arange() function
#The arange() function in numpy is same as range() function.
#arange(start, end, step)

from numpy import*

# new=arange(10)
# print(new)


even=arange(2,11,2)
print(even)
print("The array elements are:")
for i in even:
    print(i,end=" , ")

odd=arange(1,11,2)
print("The array elements are:")

for i in odd:
    print(i,end=" , ")