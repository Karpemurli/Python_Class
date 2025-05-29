# 1.	Write a Python program to create a simple class Person with a name attribute.


class Person():
    
    def __init__(self, name):
        self.name = name
        
    def display_person(self):
        print(f'The name is= ',self.name)
        
name=input('Enter the name = ').strip().title()

obj_person=Person(name)

obj_person.display_person()