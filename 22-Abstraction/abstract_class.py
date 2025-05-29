from abc import ABC ,abstractmethod



#here I can define abstract class
class Employee(ABC):
    @abstractmethod
    def display(self): #here only we can declare the method
        pass
    
    
# can we create the object of abstract class?

emp = Employee()
    
 # o/p = TypeError: Can't instantiate abstract class Employee with abstract method display  
    