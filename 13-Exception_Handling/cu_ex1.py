# 2. Custom Exception for Dividing by Zero




class deno(Exception):
    def __init__(self, msg="Invalid input"):
        super().__init__(msg)


def dividing(nm1,number):
    if number == 0:
        raise deno("Cannot divide by zero")
    return nm1 / number


try:
    nm1 = float(input("Enter first number="))
    number =float(input("Enter a number="))
    result = dividing(nm1,number)
    print(f"Result: {result}")
except deno as err:
    print(err)
except ValueError:
    print("Invalid input. Please enter a number.")
except Exception as e:
    print(str(e))