# Question 1: Find the Largest and Smallest Numbers in a List
# Write a Python program that does the following:
# 1.	Accepts a list of integers from the user (input numbers separated by spaces).
# 2.	Finds and prints:
# o	The largest number in the list.
# o	The smallest number in the list.
# 3.	Ensure the program handles invalid inputs gracefully.

num=input("enter the number:").split()

if all(num.isdigit() for num in num):
    num=list(map(int,num))
    
    largest=max(num)
    smallest=min(num)
    
    print("largest number is:", largest)
    print("smallest number is:", smallest)

else:
    print("Invalid input")