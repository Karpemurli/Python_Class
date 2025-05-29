

# Exercise 1: Define a function that accepts 2 values and return its sum, subtraction and multiplication.

def ss(x,y):
    result1=x+y
    result2=x-y
    return result1, result2

x=int(input('Enter first value:'))
y=int(input('Enter second value:'))


result1,result2=ss(x,y)

print("Addition:",result1)
print("substraction:",result2)