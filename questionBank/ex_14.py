# 14. Write a program to check whether the last digit of a number( entered by user ) is divisible by 3 or not.
# Take user input


Number= int(input("Enter A Nmuber:"))

Last_digit=Number % 10

print("LAST NUMBER:",Last_digit)

if Last_digit % 3 == 0:
    print(f"{Number} is Divided")
else:
    print(f"{Number} is not Divided")