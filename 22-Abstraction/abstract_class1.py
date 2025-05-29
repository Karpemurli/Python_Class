from abc import ABC, abstractmethod


class Employee(ABC):
    @abstractmethod
    def totalsalary(self):
        pass
    
class Engineer(Employee):
    
    def __init__(self,name, basic_salary,bonus):
        self.name=name
        self.basic_salary=basic_salary
        self.bonus=bonus
        
        
    def totalsalary(self):
        return self.basic_salary + self.bonus
    
eng=Engineer("Ajay",2500,500)
print(eng.name)
print("The total salary is = ",eng.totalsalary())
         