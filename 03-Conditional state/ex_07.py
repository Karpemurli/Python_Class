#Write a program that prompts the user to enter their weight (in kilograms) and height (in meters). The program should calculate the Body Mass Index (BMI) using the formula:
# BMI = weight / (height * height).
# The program should then classify the BMI into one of the following categories:
# Underweight: BMI less than 18.5
# Normal weight: BMI between 18.5 and 24.9
# Overweight: BMI between 25 and 29.9
# Obesity: BMI 30 or greater

weight=float(input("Enter Your Weight in kilograms: "))
height=float(input("Enter Your Height in meters:"))

bmi=weight/(height*height)
print("BMI: " , bmi)

if bmi < 18.5:
    print("Underweight")
elif 18.5 <= bmi <= 24.9:
    print("Normal weight")
elif 25 <= bmi <= 29.9:
    print("Overweight")
elif bmi >= 30:
    print("Obesity")
else:
    print("Invalid Input")