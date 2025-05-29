# 3. Write a Python program that executes division and handles an ArithmeticError exception if there is an arithmetic error.




def main(a,b):
    
    try:
        result=a/b
        print(f"result={result}")
    except ArithmeticError as e:
        print(f"ArithmeticError: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")


nume=float(input("Enter the num:"))
deno=float(input("Enter the denominator:"))

ans=main(nume,deno)

        

