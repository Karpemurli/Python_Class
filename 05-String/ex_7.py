# 1. Write a Python program to insert space before every capital letter appears in a given word.
# Sample Data:
# ("PythonExercises") -> "Python Exercises"
# ("Python") -> "Python"
# ("PythonExercisesPracticeSolution") -> "Python Exercises Practice Solution"



str1="PythonExercises"
str2='Python'
str3='PythonExercisesPracticeSolution'




str1=input("Please enter=")

result=''
for i in str1:
    if i.isupper():
        result += " "+i.upper()
    else:
        result += i
print(result)


# print(str2)


# result3=' '
# for j in str3:
#     if j.isupper():
#         result3 +=" "+j.upper()
#     else:
#         result3 += j
# print(result3)






