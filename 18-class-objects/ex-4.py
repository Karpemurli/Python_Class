# Class and Instance Variables in Python

# Class Variables
# Instance Variables

class Dog:
    
    # Class Variable
    species = 'Canine'
    
    def __init__(self,name,age):
        # Instance Variable
        self.name = name
        self.age = age
        
#create Objects

dog1=Dog("chrlii",2)
dog2=Dog("marli",5)


# Accessing Class and Instance Variables

print(dog1.species) #class variable
print(dog1.name) #Instance variable
print(dog2.name) #instance variable


#MODIFY Instance Variables

dog1.name="Max"
print(dog1.name) #Updated instance variable


#Modify class Variables

Dog.species = "Feline"

print(dog1.species) #Updated class variable
print(dog2.species) #Updated class variable