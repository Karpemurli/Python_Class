# 15. Write a program to accept percentage from the user and display the grade according to the following criteria:

#          Marks                                    Grade
#          > 90                                         A
#          > 80 and <= 90                        B
#          >= 60 and <= 80                      C
#          below 60                                  D


percentage=int(input('Enter the percentage='))

if percentage > 90:
    grade="A"
elif 80 < percentage <=90:
    grade="B"
elif 60 <= percentage <= 80:
    grade="C"
elif percentage < 60:
    grade="D"
else:
    grade="Invalid percentage"


print(f"Grade: {grade}")    