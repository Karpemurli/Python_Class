
#Thread communication using notify() method and wait() method

from threading import *
from time import *

class Producer:
    def __init__(self):
        self.lst = []
        self.cv = Condition()
        
    def producer_data(self):
        # use the lock
        self.cv.acquire()
        for i in range(1,11):
            self.lst.append(i)
            sleep(1)
            print("Product produced completed")
            
            
        # send the notification to the consumer
        self.cv.notify()
        
        # release the lock
        self.cv.release()


class Consumer:
    def __init__(self,prod):
        self.prod=prod
        
    def consume(self):
        self.prod.cv.acquire()
        self.prod.cv.wait(timeout=0)
        self.prod.cv.release()
        
        #display the data
        print(self.prod.lst)
        
#create the object of Producer Class

p= Producer()

#create the object of Consumer Class

c= Consumer(p)


#create a two thread

t1=Thread(target=p.producer_data)
t2=Thread(target=c.consume)

# run the thread

t1.start()
t2.start()
        