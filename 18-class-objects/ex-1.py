# Using __init__() Function


class Dog:
    species = "Canine" # class attribute
    
    
    def __init__(self,name,age):
        self.name = name         #Instance attribute
        self.age = age           #Instance attribute
        
#creating an object of the dog class

dog1 =Dog("Buddy ",3)

print(dog1.name)
print(dog1.species)