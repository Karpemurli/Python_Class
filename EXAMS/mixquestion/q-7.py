# Write a program to find the maximum value in a list without using built-in functions.



num=[10,5,55,88,76,45,99,22,3,44,66,99,22,98,12,102]


max_value=num[0]

for i in num:
    if i > max_value:
        max_value=i
        
print("Maximum value in the list is:", max_value)