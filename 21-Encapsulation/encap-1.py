
class Employee:
    
    def __init__(self,name,city):
        self.name=name
        self.city=city
        
    def display_info(self):
        print("Name:",self.name,"city :",self.city)
        
        
obj_emp=Employee("Ajay","Pune")
obj_emp.display_info()