
# Synchronization

from threading import * #Thread,Lock
from time import *



class Theater:
    def __init__(self,str,lock):
        self.str = str
        self.lock = lock #shared lock 
        
    def movieShows(self):
        with self.lock:      #ensures only one thread run at time
            for i in range(1,6,1):
                print(self.str,":",i)
                sleep(1)
                
# create a single lock instance to be shared among threads

lock = Lock()

#create the object class theater

obj1=Theater("Cut Ticket",lock)

obj2=Theater("Show Chair",lock)

#create the Thread class
t1=Thread(target=obj1.movieShows)
t2=Thread(target=obj2.movieShows)


# start the thread

t1.start()
t2.start()

t1.join()
t2.join()

# output :
    
# Cut Ticket : 1
# Cut Ticket : 2
# Cut Ticket : 3
# Cut Ticket : 4
# Cut Ticket : 5
# Show Chair : 1
# Show Chair : 2
# Show Chair : 3
# Show Chair : 4
# Show Chair : 5

                


