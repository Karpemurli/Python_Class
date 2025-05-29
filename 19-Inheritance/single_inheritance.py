
# Parent class
class Vehicle:
    def info(self):
        print(" Inside the vehicle class ")
        
# Child class
class Car(Vehicle):
    
    def  car_info(self):
        print(' Inside the car class')
        
# Inheritance always create object of child class

car_obj = Car()

car_obj.info()
car_obj.car_info()