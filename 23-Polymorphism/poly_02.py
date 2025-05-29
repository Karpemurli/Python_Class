# Polymorphism using method overriding method


class shape:
    def area(self):
        pass
    
class rectangle(shape):  
    def __init__(self,l,w):
        self.l=l
        self.w=w
        
    def area(self):
        return self.l * self.w
    
class Circle(shape):
    
    def __init__(self,r):
        self.r=r
        
    def area(self):
        return 3.14 * (self.r ** 2) #3.14 * self.r * self.r
    
    
rect_angle = rectangle(2,6)
cir=Circle(4)

print("Area of rectangle is:", rect_angle.area())

print("Area of circle is:", cir.area())

   
    
    
  

