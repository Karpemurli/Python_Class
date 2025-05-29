from platform import uname
from random import choice
import pymysql as ss
from django.template.defaultfilters import title
from pygetwindow._pygetwindow_win import cursor
from tabulate import tabulate
from dotenv import load_dotenv
import os
import pyautogui

load_dotenv()
my_password = os.getenv("db_pass")

def connect_db():
    return ss.connect(host='localhost',user='root',passwd=my_password,database='library_db')

def commit_message(cursor,db,message):
    db.commit()
    print(message)

#  Login ________________________

def login(cursor):
    while True:
        uname=input("Enter username: ").strip()
        upass=pyautogui.password(text="Enter password: ",title="Login",mask='*')
        cursor.execute("select * from users where uname =%s and password=%s",(uname,upass))

        if cursor.fetchone():
            print(f"Welcome {uname}!")
            return True
        else:
            print("Invalid username or password")

#________Book Mng._________________________

def add_book(cursor,db):
    while True:
        title=input("Enter Book Title : ").title()
        author=input("Enter Book Author : ").title()
        genre=input("Enter Book Genre : ").title()
        available=int(input("Enter Quantity Available : "))
        cursor.execute("insert into books(title,author,genre,available) values (%s,%s,%s,%s)",(title,author,genre,available))
        commit_message(cursor,db," Book Added.")

        another =input("Add Another Book ? (y/n) ").lower().strip()
        if another != "y":
            break


def update_book(cursor,db):
    book_id =int(input("Enter Book ID to Update: "))
    title = input("Enter Book Title : ").title()
    author = input("Enter Book Author : ").title()
    genre = input("Enter Book Genre : ").title()
    available = int(input("Enter Quantity Available : "))
    cursor.execute("update books set title=%s,author=%s,genre=%s,available=%s where book_id=%s",(title,author,genre,available,book_id))
    commit_message(cursor,db," Book Updated.")


def delete_book(cursor,db):
    book_id = int(input("Enter Book ID to Delete: "))
    cursor.execute("delete from books where book_id=%s",(book_id,))
    commit_message(cursor,db," Book Deleted.")



def view_books(cursor,db):
    cursor.execute("select * from books")
    result=cursor.fetchall()
    print(tabulate(result,headers=["Book ID","Title","Author","Genre","Available"],tablefmt='psql'))


def book_menu(cursor,db):
    while True:
        print("\n-----Book Menu-----")
        print("1. Add Book")
        print("2. Update Book")
        print("3. Delete Book")
        print("4. View Books")
        print("5. Back Menu")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_book(cursor, db)
        elif choice == "2":
            update_book(cursor, db)
        elif choice == "3":
            delete_book(cursor, db)
        elif choice == "4":
            view_books(cursor, db)
        elif choice == "5":
            break
        else:
            print("Invalid choice")


#_________User Mng_______________________

def user_register(cursor,db):
    name=input("Enter full name :").title()
    uname=input("Enter username : ")
    upass=pyautogui.password(text="Enter password: ")
    cursor.execute("insert into users(name,uname,password) values (%s,%s,%s)",(name,uname,upass))
    commit_message(cursor,db," User Registered.")

def search_books(cursor,db):
    keyword =input("Enter book title/author/genre : ")
    cursor.execute("select * from books where title like %s or author like %s or genre like %s",(f'%{keyword}%',f'%{keyword}%',f'%{keyword}%'))
    result=cursor.fetchall()
    print(tabulate(result,headers=["Book ID","Title","Author","Genre","Available"],tablefmt='psql'))

def request_borrow(cursor,db):
    book_id=int(input("Enter Book ID : "))
    user_name=input("Enter username : ")
    cursor.execute("insert into requests(uname,book_id,status) values (%s,%s,%s)",(user_name,book_id,"Pending"))
    commit_message(cursor,db," Request Submitted.")

def user_menu(cursor, db):
    while True:
        print("\n-----User Menu-----")
        print("1. Register")
        print("2. Search Book")
        print("3. Request Borrow")
        print("4. Back Menu")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            user_register(cursor, db)
        elif choice == "2":
            search_books(cursor, db)
        elif choice == "3":
            request_borrow(cursor, db)
        elif choice == "4":
            break
        else:
            print("Invalid choice")





#____________Main Menu____________________

def main_menu():
    db=connect_db()
    cursor=db.cursor()

    if not login(cursor):
        return
    while True:
        print("\n---Library Main Menu---")
        print("1. Book management")
        print("2. User Services")
        print("3. Exit")

        choice=input("Enter your choice: ").strip()
        if choice == "1":
            book_menu(cursor,db)
        elif choice == "2":
            user_menu(cursor,db)
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main_menu()




