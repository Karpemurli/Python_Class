# 9)	Write a Python program that prompts the user to enter a positive integer. Your program should display all the factors of the number. Additionally, calculate and display the sum of its factors.

# Sample output: Enter a positive integer: 45 
# Factors: 1 3 5 9 15 45 
# Sum of factors: 78


nm=int(input("Enter a positive Number:"))


sum_of_factors=0

print("Factors:",end= " ")

for i in range(1,nm+1):
    if nm%i==0:
        print(i,end= " ")
        sum_of_factors+=i


print(f"\nSum of factors:{sum_of_factors}")

