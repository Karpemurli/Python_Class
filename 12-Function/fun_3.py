#function returns multiple values/results

def DoTask(num1,num2):
    add_results=num1+num2
    sub_results=num1-num2
    mulia_results=num1 * num2
    
    return add_results,sub_results,mulia_results


Add=int(input("Enter the num1="))
Add1=int(input("Enter the num2="))

add,sub,mul=DoTask(Add,Add1)


print("The addition is=",add)
print("The sub is=",sub)
print("The mul is=",mul)
    