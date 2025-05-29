
#Base class (Parent class)

class Vehicle:
    
    def vehicle_info(self):
        print('Inside Vehicle class')

class Car(Vehicle):
    
    def car_info(self):
        print('Inside from car')
        
class SportCar(Car):
    
    def sport_info(self):
        print('Inside  the sport car ')
        
# create always the object child class # SportCar

sport_obj = SportCar()

sport_obj.vehicle_info()
sport_obj.car_info()
sport_obj.sport_info()



    