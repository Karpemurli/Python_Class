# 17.Write a program to check whether a number entered is three digit number or not.


num=int(input("Enter a Number:"))

new_num=str(num)#convert the num to string



if len(new_num) == 3:
    print("The Number entered has 3 digits.")
else:
    print("The Number entered is not 3 digits.")


# num =input('Enter a Number=')


# if num.isdigit() and len(num) == 3:
#     print('The Number entered has 3 digits.')
# else:
#     print('The Number entered is not 3 digits.')

