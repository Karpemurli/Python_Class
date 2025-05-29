
# solving deadlock 

# DeadLock 

from threading import Thread,Lock
from time import time,sleep

#create a two lock
rahul_phone = Lock()
shyam_phone = Lock()


def rahul_calls_shyam():
    print("Rahul calling Shyam...")
    with rahul_phone:
        sleep(1)
        print("Rahul picks the call of shyam")
    with shyam_phone:
        print("Rahul and Shyam are taking")

def shyam_calls_rahul():
    print("Shyam calling Rahul")
    with rahul_phone:
        sleep(1)
        print("shyam picks the call of Rahul")
    with shyam_phone:
        print("shyam and Rahul are taking")
        
        
# create the two thread

t1=Thread(target=rahul_calls_shyam)
t2=Thread(target=shyam_calls_rahul)

t1.start()
t2.start()

t1.join()
t2.join()

print("Call discussion complete")
        
        

    
        
        