# DeadLock 

from threading import Thread,Lock
from time import time,sleep

#create a two lock
rahul_phone = Lock()
shyam_phone = Lock()


def rahul_calls_shyam():
    print("Rahul calling Shyam...")
    rahul_phone.acquire()
    sleep(1)
    
    print("Rahul is waiting for shyam to answer")
    shyam_phone.acquire()
    print("Rahul and Shyam are taking")
    shyam_phone.release()
    rahul_phone.release()
    
def shyam_calls_rahul():
    print("Shyam calling Rahul")
    shyam_phone.acquire()
    sleep(1)
    
    print("Shyam is waiting for Rahul to answer")
    rahul_phone.acquire()
    
    print("Shyam And Rahul are taking")
    rahul_phone.release()
    shyam_phone.release()
    
    
# create the two thread

t1=Thread(target=rahul_calls_shyam)
t2=Thread(target=shyam_calls_rahul)

t1.start()
t2.start()

t1.join()
t2.join()

print("Call discussion complete")


# output=

# Rahul calling Shyam...
# Shyam calling Rahul                        # dogha ekamekala wait karat ahe tyamul deadlock tayar zala
# Rahul is waiting for shyam to answer
# Shyam is waiting for Rahul to answer



#solving the problem in Thread_08.py

    
    
    
    

