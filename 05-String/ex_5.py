# Write a Python program to change a given string to a newly string where the first and last chars have been exchanged.

str_a='Gold'
new_string=(str_a)


if len(str_a)>1:
    new_string=str_a[-1]+str_a[1:3]+str_a[0]
else:
    new_string=str_a

print('Old string=',str_a)
print('New String=',new_string)

# print(str_a[-1]+str_a[1:3]+str_a[0])





