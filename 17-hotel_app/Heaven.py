import pymysql as pysql
from tabulate import tabulate
from dotenv import load_dotenv
import os
import pyautogui



load_dotenv()

my_password=os.getenv('db_pass')
# print(my_password)


def connect_db():
    return pysql.connect(host='localhost',user='root',passwd=my_password,database='heaven')


def commit_and_message(cursor,db,message):
    db.commit()
    print(message)
    
    
#______________Login _________________

def login(cursor):
    while True:
        uname=input('Enter the username = ')
        upass=pyautogui.password(text="Enter the user password: ",title='Enter Password',default='',mask='*')
        cursor.execute('select * from login where name= %s and password =%s',(uname,upass))
        
        user=cursor.fetchone()
        
        if user:
            print('Login sucess welcome'+uname)
            return True
        else:
            print('Invalid username or password Please try again')
            
        break








