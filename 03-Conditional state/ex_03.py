#Write a program that prompts the user to enter their age and prints the corresponding age group. The program should use the following age groups:

# 0-12: 		Child
# 13-19: 		Teenager
# 20-59: 		Adult
# 60 and above: 	Senior Citizen

age=int(input("Enter your age:"))

if age >= 0 and age <= 12:
    print("Child")
elif age >= 13 and age <= 19:
    print("Teenager")
elif age >= 20 and age <=59:
    print("Adult")
elif age >= 60 and age <=100:
    print("Senior Citizen")
else :
    print("invalid")

    

    
    
    
    


    
