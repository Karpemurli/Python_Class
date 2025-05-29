#The marks obtained by a student in 3 different subjects are input by the user. Your program should calculate the average of subjects and display the grade. The student gets a grade as per the following rules:

# Average	Grade
# 90-100	A
# 80-89	B
# 70-79	C
# 60-69	D
# 0-59	F

Python=int(input("Enter the mark of python out of 100="))
Java=int(input("Enter the mark of Java out of 100="))
R=int(input("Enter the mark of R out of 100="))

Sum=Python+Java+R
print("Total Mark=",Sum)

avg=Sum /3
print("Percentage=",avg)

if avg>=90 and avg <= 100:
    print("Grade: A")
elif avg >=80 and avg <=89:
    print("Grade: B")
elif avg >=70 and avg <=79:
    print("Grade: C")
elif avg >=60 and avg <=69:
    print("Grade: D")
elif avg >=0 and avg <= 59:
    print("Fail")
else:
    print("Invalid")
