# __str__ Method


# __str__ method in Python allows us to define a custom string representation of an object.


class Cat:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
    def __str__(self):
        return f"{self.name} is {self.age} Years Old ."  #Correct :Returning a string
    

cat1 = Cat("Tom", 3)
cat2 = Cat("Buddy",6)

print(cat1)  # Output: Tom is 3 Years Old.
print(cat2)
        