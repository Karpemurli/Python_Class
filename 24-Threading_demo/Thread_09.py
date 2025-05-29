

# Thread communication

from threading import *
from time import time,sleep


# create the Producer class
class producer:
    def __init__(self):
        self.lst=[]
        self.dataProvider = False
        
    def producer_data(self):
        for i in range(1,11,1):
            self.lst.append(i)
            sleep(1)
            print("Product Produced")
     
        # Inform the consumer that the production data completed.   
        self.dataProvider = True
         
        
class Consumer:
    def __init__(self,prod):  #prod - producer_data data use krnar
        self.prod = prod
    def consume(self):
        #sleep for 100 ms to check the dataProvider value
        while self.prod.dataProvider == False:
            sleep(0.1) #100 ms(mily second)
            # print(self.prod.lst)
        print(self.prod.lst)   
            
            
#create the object of Producer Class

p= producer()

#create the object of Consumer Class

c= Consumer(p)


#create a two thread

t1=Thread(target=p.producer_data)
t2=Thread(target=c.consume)

# run the thread

t1.start()
t2.start()
        