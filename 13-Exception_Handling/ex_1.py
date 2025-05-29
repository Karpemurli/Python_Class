

# def operation(num1,num2):
    
#     result=num1+num2
#     return result

# result=operation(15,85)
# print(result)
        
        
        
        
        
    
        
# def operation(num1,num2):
#     try:
#         result=num1+num2
#         return result
#     except Exception as e:
#         return str(e)

# try:
#     result=operation(15,85)
#     print(result)
# except Exception as e:
#     print(str(e))




def op(*num):
    try:
        add,sub=0,0
        for i in num:
            add += i
            sub -= i
        return add,sub
    except Exception as w:
        return str(w)

try:
    add,sub=op(15,85,90,25)
    print(add,sub)
except Exception as e:
    print(str(e))
    

    