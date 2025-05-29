# # 5.	Write a Python program to create a class with an attribute and a method that modifies its value.


class Counter():
    
    def __init__(self):
        self.count = 0
        
    def increment(self):
        self.count += 1
        
    def display(self):
        print(f"Current Count: {self.count}")
        
obj_counter = Counter()

obj_counter.increment()
obj_counter.increment()
obj_counter.increment()

obj_counter.display() 
