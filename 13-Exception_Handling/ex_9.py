# Write a Python program that prompts the user to input an integer and raises a ValueError exception if the input is not a valid integer.



def integer():
    try:
        user=input('enter a number=')
        return int(user)
    except ValueError:
        print('\ninvalid input')
        return None
    
    except Exception as s:
        return str(s)
    

num=integer()
print(num)

# try:
#     # Code that might raise a ValueError
#     number = int(input("Enter a number: "))
#     print(f"You entered: {number}")
# except ValueError as e:
#     # Handle the ValueError
#     print(f"ValueError encountered: {e}")

            