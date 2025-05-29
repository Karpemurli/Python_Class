# 5. Write a program that prompts the user to enter their age and prints the corresponding age group. The program should use the following age groups:

# 0-12: 		Child
# 13-19: 		Teenager
# 20-59: 		Adult
# 60 and above: 	Senior Citizen


age=int(input("Enter Your Age:"))

if 0 <= age <=12:
    print("child")
elif 13 <= age <= 19:
    print('Teenager')
elif 20 <= age <= 59:
    print('Adult')
elif 60 >= age:
    print('Senior citizen')

