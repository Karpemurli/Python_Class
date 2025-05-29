# 7. Write a program that prompts the user to enter their weight (in kilograms) and height (in meters).
# The program should calculate the Body Mass Index (BMI) using the formula: BMI = weight / (height * height). 
# The program should then classify the BMI into one of the following categories:

# less than 18.5 - Underweight		
# BMI between 18.5 and 24.9 - Normal weight 	
# BMI between 25 and 29.9 - Overweight		
# BMI 30 or greater - Obesity


def program(height,weight):
    
    BMI=weight /(height * height)
    print(f"BMI= ",BMI)
    
    
    if BMI < 18.5:
        print("Underweight")
    elif 18.5 <= BMI <= 24.8:
        print("Normal weight")
    elif 25 <= BMI <= 29.9:
        print("Overweight")
    elif BMI >= 30:
        print('obesity')
    else:
        print('Invalid')
        
    return BMI

height=float(input('Enter your height in km: '))
weight=float(input('Enter your weight in m: '))


program(height,weight)






# weight=float(input("Enter Your weight in Kilometers:"))
# height=float(input("Enter Your Height in meters:"))

# BMI=weight/(height*height)
# print("BMI:",BMI)

# if BMI < 18.5:
#     print("Underweight")
# elif 18.5 <= BMI <= 24.9:
#     print("Normal weight")
# elif 25 <= BMI <= 29.9:
#     print("Overweight")
# elif BMI >= 30:
#     print("obesity")
# else:
#     print("Invalid")
    