#Question 2: Student Grades Classification
#Write a Python program to classify students’ grades based on their scores:
#.	Accept scores of 5 students as input (0 to 100).
#2.	Use the following classification:
#o	90 and above: Grade A
#o	80–89: Grade B
#o	70–79: Grade C
#o	Below 70: Grade F
#3.	Output each student’s grade in the format: Student 1: Grade B.1


for i in range(1,6):
    score=int(input("enter the number of students(0-100):"))
    
    
    
    if score >= 90:
        grade='A'
    elif score >=80:
        grade='B'
    elif score >=70:
        grade='C'
    else:
        grade='Failed'
    
    print(f"Student= {i} :Grade= {grade}")
    
    
