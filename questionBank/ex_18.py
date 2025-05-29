# 18. Q1. Accept the following from the user and calculate the percentage of class attended:
# a.     Total number of working days.
# b.     Total number of days for absent.
#     After calculating percentage show that, If the percentage is less than 75, than student will not be able to sit in exam.

working_days =int(input("Working days="))
absent_days=int(input("Enter the working Days Absent="))

Attended_days =working_days - absent_days

print(f'Total Attended Days: {Attended_days}')

per=(Attended_days/working_days)*100

print(f'\nAttendance Percentage:{per:}%')

if per < 75:
    print('You are not allowed to sit in the exam as your attendance is less than 75%.')
else:
    print('You are allowed to sit in the exam')



