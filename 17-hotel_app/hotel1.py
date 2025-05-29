import pymysql as pysql
from dotenv import load_dotenv
from tabulate import tabulate
import os
import pyautogui





# load_dotenv("D:/python/17-hotel_app/.env") #file path =  .env file
load_dotenv()

my_password =os.getenv("db_pass")
# print(my_password)   


def connect_db():
    return pysql.connect(host="localhost",user="root",passwd=my_password,database="hotel_db")

def commit_and_message(cursor,db,message):
    db.commit()
    print(message)
    
    
#______________Category code started_________________________



def login(cursor):
    while True:
        uname=input("Enter the username = ")
        upass=pyautogui.password(text="Enter the User Password=", title="Enter Password",default="",mask="*")
        cursor.execute("select * from user_login where uname=%s and password=%s",(uname,upass))
        user=cursor.fetchone()
        
        if user:
            print("Login Successful  Welcome "+ uname)
            return True
        
        else:
            print("Invalid username and password please check again")
            
            
def main_menu():
    db=connect_db()
    cursor=db.cursor()
    
    if not login(cursor):
        return
    
    while True:
        print("\n Main Menu")
        print("1. Add Category")
        print("2. Add Products")
        print("3. Add Orders")
        print("4. Exit from your choice =")
        
        choice=input("Enter Your Choice=")
        
        
        if choice == '1':
            print("This is category")
        elif choice == '2':
            print("This is product")
        elif choice == '3': 
            print("This is orders")
        elif choice == '4':
            break
        else:
            print("Enter proper choice")            


if __name__ ==  "__main__":
    main_menu()
    
        
        

    
    

    











