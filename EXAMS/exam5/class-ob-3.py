# 3.	Write a program to create a class Student with a parameterized constructor to initialize name and age.



class Student():
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def initialize(self):
        print(f'Student Name: {self.name}, Age: {self.age}')
        
name=input('Enter the name of the student = ').strip().title()
age=int(input('Enter the age of the student = '))

obj_student=Student(name,age)
obj_student.initialize()