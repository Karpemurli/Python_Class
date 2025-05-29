# 3. Creating a thread without creating subclass to thread class:

# without creating thread class
from threading import *

class MyThread():
    def __init__(self,str):
        self.str = str
        
    # define one method
    def display(self,n1,n2):
        print(self.str)
        print("Print value = ",n1,n2)
        
# creating the object of MyThread class

obj= MyThread("My Values ")

t1=Thread(target=obj.display,args=(12,51))

t1.start()
 