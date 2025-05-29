#Thread_using object

from threading import *
import time
from time import sleep

#1. Creating thread without using class:

#create the functions

def printEven():
    for i in range(11):
        if i % 2 == 0:
            print("Even = ",i)
            sleep(1)
            
def printOdd():
    for i in range(10):
        if i % 2 == 1:
            print("Odd = ",i)
            sleep(1)
            
            
#calculation the start time

start_time=time.time()


#creating the object of thread class

t1= Thread(target=printEven())
t2= Thread(target=printOdd())


t1.start()
t2.start()

t1.join()
t2.join()


end_time=time.time()


final_time= end_time - start_time

print(f"Total Execution Time= {final_time:.2f}seconds")