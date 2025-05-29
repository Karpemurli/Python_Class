# Exercise 2: Define a function that accepts roll number and returns whether the student is present or absent.




def checkpresenty(rollnumber,present_student):
    
    if rollnumber in present_student:
        return 'Present'
    else:
        return 'Not Present'
    
present_student = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]

roll_number =int(input('enter roll number:'))

status=checkpresenty(roll_number,present_student)


print(f"Roll number {roll_number} is {status} present.")        
    