class Person:
    
    #here I can define the parameterized Constructor
    
    def __init__(self,name,city,age):
        
        #here I can define the parameterized Constructor
        self.name=name
        self.city=city
        self.age=age
        
        
    def displaydata(self):   #this is the method
        print('The name is = ',self.name)
        print('The city is = ',self.city)
        print('The age is = ',self.age)
        
# here i can define the object of the class, When we define the object of the class the constructor will automatically called.

pname=input('Enter the name of the person = ')
pcity=input('Enter the city of the person = ')
page=int(input('Enter the age of the person= '))

obj_person=Person(pname,pcity,page)
obj_person.displaydata()        

     