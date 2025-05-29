# 4.	How can you create a class with multiple methods, including one for setting values and another for displaying them?


class Student():
    def values(self, name, age):
        
        self.name = name
        self.age = age
        
    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")
        

name=input('Enter the name of the student = ').strip().title()
age=int(input('Enter the age of the student = '))


student_obj = Student()

student_obj.values(name, age)
student_obj.display()