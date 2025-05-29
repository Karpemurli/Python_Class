
#try with else block

def divide_number(num1, num2):
    try:
        result=num1 /num2
    except ZeroDivisionError :
        print("Error: Division by zero is not allowed.")
    else:
        print("Division successful....! The result is = ",result)
        
divide_number(20,5)
        
divide_number(20,0)