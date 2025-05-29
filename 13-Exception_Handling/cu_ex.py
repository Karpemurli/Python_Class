
# 1. Custom Exception for Age Validation


class demo(Exception):
    def __init__(self, msg=f"Invalid Age."):
        super().__init__(msg)
    
    
def AgeValidation(Age):
    if Age <= 0 or Age >= 120:
        raise demo(f"Invalid Age {Age}.")
    return f"Age {Age} is valid..."

try:
    Age=int(input("Enter Your Age: "))
    print(AgeValidation(Age))
    
except demo as e:
    print(str(e))
except ValueError as e:
    print("Enter a number...")
except Exception as e:
    print(f"An error occurred: {e}")
else:
    print("\n\nAge validation passed.")
finally:
    print("\n\nAge validation finished.")
    
    