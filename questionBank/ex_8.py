# 8. The marks obtained by a student in 3 different subjects are input by the user. 
# Your program should calculate the average of subjects and display the grade. 
# The student gets a grade as per the following rules:

# Average	Grade
# 90-100	A
# 80-89	B
# 70-79	C
# 60-69	D
# 0-59	F

maths=int(input('Enter the maths mark (0-100)='))
english=int(input('Enter the English mark (0-100)='))
Marathi=int(input('Enter the Marathi mark (0-100)='))

add=maths+english+Marathi
avg=add/300*100

print("Total Marks=",add)
print("Percentage=",round(avg,2))




if 90 <= avg <= 100:
    print('Grade A')
elif 80 <= avg <= 89:
    print('Grade B')
elif 70 <= avg <=79:
    print('Grade C')
elif 60 <= avg <=69:
    print('Grade D')
elif 0 <= avg <=59:
    print('Grade F')
else :
    print("invalid")