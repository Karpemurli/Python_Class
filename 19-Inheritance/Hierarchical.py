

#one parent class

class Vehicle:
    
    def vehicle_type(self):
        return 'This is a Vehicle'


# child class    
class Car(Vehicle):
    
    def car_features(self):
        return 'Car Runs on road'
    
class Truck(Vehicle):
    
    def truck_features(self):
        return 'Truck is heavy'
    
#objects

obj_car = Car()
obj_truck = Truck()

print(obj_car.vehicle_type())
print(obj_car.car_features())
print(obj_truck.vehicle_type())
print(obj_truck.truck_features())