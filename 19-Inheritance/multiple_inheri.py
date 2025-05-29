#parent class

class Person:
    
    def person_info(self,name,age):
        print('Inside the Person class')
        print(f'Name= ',name, 'age= ',age)
 
#parent class        
class Company:
    
    def company_info(self,comapny_name,location):
        print('Inside the Company class')
        print(f'Name= ',comapny_name, 'location= ',location)
 
# child class        
class Employee(Person,Company):
    
    def employee_info(self,salary,skill):
        print('Inside the Employee class')
        print(f'Salary = ',salary, 'skill= ',skill)
        
#object in child class

emp_obj = Employee()

emp_obj.person_info('Murali',24)
emp_obj.company_info('code crafter','Kolhapur')
emp_obj.employee_info(25000,'emp')
        
        
        