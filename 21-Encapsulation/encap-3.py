
#Protected member 

# # Protected varible writing  using _ single underscore 

class Company:
    def __init__(self):
        self._project = "MLP"  # Protected variable
        
class Employee(Company):
    def __init__(self,name):
        
        self.name=name
        # super().__init__()
        Company.__init__(self)
        
    def show(self):
        print("The Name is = ",self.name)
        print("The Project name is = ",self._project) #here we can use protected memeber
        
obj_emp = Employee("SANSKAR")
obj_emp.show()
        
