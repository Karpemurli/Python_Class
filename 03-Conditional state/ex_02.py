#Write a program that prompts the user to enter a number and determines whether it is positive, negative, or zero. The program should print "Positive" if the number is greater than 0, "Negative" if the number is less than 0, and "Zero" if the number is 0.

num = int(input("Enter a number:"))
 
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")
    
    
 