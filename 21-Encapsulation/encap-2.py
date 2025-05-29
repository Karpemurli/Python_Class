class Emp:
    def __init__(self,name,salary):
        self.name=name                #Public
        self.__salary=salary          #Private Variable
    
    #How we can access the private memeber?
    #The private member can be accessed by creating public methods.
    
    def show_salary(self):
        print("The salary is= ",self.__salary)
        
# we are creating the object of class of access the salary variable

obj_emp=Emp("ajay",25000)
print("The Name =",obj_emp.name)
# print("The salary = ",obj_emp.__salary)  #AttributeError: 'Emp' object has no attribute '__salary'
obj_emp.show_salary()



# # private varible writing  using __ double underscore 