
# Polymorphism using method overloading method

class Calculator:
    def add(self,a,b,c=0,d=0):
        return a + b  + c + d    
    
calc=Calculator()

result1=calc.add(1,3)
result2=calc.add(1,4,5)
result3=calc.add(1,4,15,25)

print(result1)
print(result2) 
print(result3)

