# 2. Creating a thread by creating a subclass to thread class:

# creating subclass

from threading import *



class MyThread(Thread):
    # override run() method is present in Thread class 
    def  run(self):
        for i in range(1,11):         #not returning output
            print(i)
            
    def  run(self):                    # latest printing output
        for i in range(1,5):
            print(i)
            
    def add(self):                        # separate calling object
        print('Addition: ',10+20)
        
        
class Mythread2(Thread):
    def  run(self):
        for i in range(11,21):
            print(i)
            
# object  of creating of MyThread class

t1=MyThread()
t2=Mythread2()

t1.start()
t1.join()

t2.start()
t2.join()
