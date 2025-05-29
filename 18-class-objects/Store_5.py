

# # # Store 5 Persons data
# # # here i can create the list to store the names of the person



# # # person_list=[]

# # # class Person:
    
    
# # #     def __init__(self,name):
        
# # #         self.name = name
        
        
# # #     def show_person(self):
        
# # #         print("_____________________________________________________")
        
# # #         for per in person_list:
# # #             print(per.name)
        
        
# # # #input 5 person data

# # # for i in range(5):
# # #     pname=input(f'Enter the name of the person {i+1} = ')
# # #     person_list.append(Person(pname))
    

# # # # create the object of the class and called show() method.

# # # obj_preson=Person(person_list)
# # # obj_preson.show_person()

person_list=[]

class Person:
    
    def __init__(self,name,city,age):
        
        self.name = name
        self.city = city
        self.age = age
        
    def show_data(self):
        
        print("_____________________________________________________")
        print(f"Name : {self.name},  City : {self.city},  Age : {self.age}")
        
for i in range(5):
    pname=input(f'Enter the person name {i+1}: ')
    pcity=input(f'Enter the person city {i+1}: ')
    page=int(input(f'Enter the person age {i+1}: '))
    
    
    
    person_list.append(Person(pname,pcity,page))
    
    
print("\nStored Persons data: ")

for person in person_list:
    person.show_data()


