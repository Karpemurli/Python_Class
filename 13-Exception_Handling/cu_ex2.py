# 3. Custom Exception for Invalid Input





class inavalidinput(Exception):
    def __init__(self, msg="Invalid Input"):
        super().__init__(msg)

def digit(Number):
    if not Number.isdigit():
        raise inavalidinput( " digit must be a number")
    return int(Number)

try:
    Number=input("Enter A Number:")
    result=digit(Number)
    print("Number:", result)
except inavalidinput as e:
    print(e)
except Exception as e:
    print(str(e))
else:
    print("Success!")
finally:
    print("Program Ended")
    