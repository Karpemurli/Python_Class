# 1. Write a Python program to handle a ZeroDivisionError exception when dividing a number by zero.


def div_num(num1,num2):
    try:
        result=num1/num2
        print(result)
    except ZeroDivisionError:
        print("Error: not divisible by zero")


num1=int(input('Enter First Number='))
num2=int(input('Enter First Number='))

div_num(num1,num2)