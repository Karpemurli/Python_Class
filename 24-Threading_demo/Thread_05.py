

# Synchronization ,Race Condition 

from threading import *
from time import *

class Theater:
    def __init__(self,str):
        self.str=str
        
        
    def movieShow(self):
        for i in range(1,6,1):
            print(self.str,":",i)
            sleep(1)
            
obj1 = Theater("Cut Ticket")
obj2 = Theater("Show Chairs")


t1=Thread(target=obj1.movieShow)
t2=Thread(target=obj2.movieShow)


t1.start()
t2.start()

# output :

# Cut Ticket : 1
# Show Chairs : 1
# Cut Ticket : 2
# Show Chairs : 2
# Cut Ticket : 3
# Show Chairs : 3
# Show Chairs : 4
# Cut Ticket : 4
# Cut Ticket : 5
# Show Chairs : 5



        


