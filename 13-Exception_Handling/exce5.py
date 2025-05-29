# raising exception


#built in

def divide_number(num1,num2):
    if num2 == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return num1 / num2

try:
    result= divide_number(10,0)
    print(result)
except ZeroDivisionError as e:
    print(str(e))
else:
    print("Finally I am executing..")