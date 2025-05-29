#5.	Write a python program to find largest number among three numbers

num1=int(input("Enter a First Number="))
num2=int(input("Enter a Second Number="))
num3=int(input("Enter a Third Number="))


if num1 >= num2 and num1 >= num3:
    largest = num1
elif num2 >= num1 and num2 >= num3:
    largest = num2 
else:
    largest =num3

print("Largest Number=", largest)





