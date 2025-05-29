# 3. Write a Python program to get the largest number from a list.

mylist=[40,5,55,60]

largest_number=mylist[0]

for num in mylist:
    if num > largest_number:
        largest_number=num
print('Largest Number=',largest_number)