from abc import ABC,abstractmethod


class calculations(ABC):
    
    # abstractmethod
    @abstractmethod
    def calculate(self,x,y):
        pass
    
#define the subclasses with thair own implmentation

class Addition(calculations):
    
    def calculate(self, x, y):
        return x + y
    
class Subtraction(calculations):
    
    def calculate(self, x, y):
        return x - y
    
class Multiplication(calculations):
    
    def calculate(self, x, y):
        return x * y
    
class Divigen(calculations):
    
    def calculate(self, x, y):
        return x / y
    
    
# create the object of each class

obj_add =Addition()
obj_sub = Subtraction()
obj_Mul=Multiplication()
obj_Divi=Divigen()

# call each method within the class

add_result=obj_add.calculate(20,30)
Sub_result=obj_sub.calculate(30,5)
Mul_result=obj_Mul.calculate(10,50)
Div_result=obj_Divi.calculate(20,10)

#print the result 

print("Addition = ",add_result)
print("Substraction= ",Sub_result)
print("Multiplication = ",Mul_result)
print("Divigen= ",Div_result)    

    
    
     