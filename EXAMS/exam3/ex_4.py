# 4. Build a program that can perform basic arithmetic operations (addition, subtraction, multiplication, division) using functions.

def operation(num1,num2):
    add=num1+num2
    sub=num1-num2
    mul=num1*num2
    div=round(num1/num2,1)
    
    return add,sub,mul,div

num1=int(input("Enter the First Number:"))
num2=int(input("Enter the Second Number:"))

Add,sub,mul,div=operation(num1,num2)

print("Addition Result:",Add)
print("Subtraction Result:",sub)
print("Multiplication Result:",mul)
print("Division Result:",div)