# Question 4: Sum of Even and Odd Numbers Using Loops
# Write a Python program to calculate the sum of even and odd numbers:
# 1.	Accept a range of numbers from the user (e.g., 1 to 100).
# 2.	Use a loop to calculate:
# o	The sum of all even numbers in the range.
# o	The sum of all odd numbers in the range.
# 3.	Print both results.


start, end=map(int,input("enter the number:").split())

even_sum = 0
odd_sum=0

for num in range(start, end+1):
    if num % 2 == 0:
        even_sum += num
    else:
        odd_sum += num
        
print(f"Sum of even numbers: {even_sum}")
print(f"Sum of odd numbers: {odd_sum}")