# 11. Write a program that prompts the user to input a year 
# and determines whether the year is a leap year or not. 
# Leap years are any years that can be evenly divided by 4. 
# A year that is evenly divisible by 100 is a leap year only if it is also evenly divisible by 400.

year=int(input('Enter the Year:'))

if (year % 4 == 0 and year % 100 != 0) or(year % 400 == 0):
    print("Leap Year=", year)
else:
    print("Not a Leap Year=", year)