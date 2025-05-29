# Self Parameter
# self parameter is a reference to the current instance of the class.
# 
# It allows us to access the attributes and methods of the object.


class Dog:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
        
    def bark(self):
        print(f"{self.name} is Barking!")
        
# Creating an instance of the Dog class
dog1 = Dog("Buddy",3)
dog1.bark()
        