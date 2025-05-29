import pymysql as pysql
from dotenv import load_dotenv
from tabulate import tabulate
import os
import pyautogui
from datetime import datetime



load_dotenv()

my_password=os.getenv("db_pass")
# print(my_password)


def connect_db():
    return pysql.connect(host='localhost',user='root',passwd=my_password,database="hotel_db")

def commit_and_message(cursor,db,message):
    db.commit()
    print(message)
    
#______________Category code started_________________________

def login(cursor):
    while True:
        uname=input("Enter the username = ")
        upass=pyautogui.password(text="Enter the user password: ",title="Enter password",default='',mask='*')
        cursor.execute("Select * from user_login where uname = %s and password =%s",(uname,upass))
        
        user=cursor.fetchone()
        if user:
            print('Login success Welcome' + uname)
            return True
        else:
            print('Invalid username and password Please check again')
            
            


def add_category(cursor,db):
    while True:
        category_name=input('Enter the category name= ').capitalize().strip() #dosa ----->Dosa
        
        cursor.execute('select count(*) from category where name =%s',(category_name))
        if cursor.fetchone()[0] > 0:
            print(f'Category {category_name} is already exists')
        else:
            cursor.execute('insert into category (name) values(%s)',(category_name))
            commit_and_message(cursor,db,"Data inserted successfully")
            display_category(cursor,db)
        result=input('Do you want to add another category? (yes/no) =').strip().lower()
        if result == 'no':
            break
            # return ## Exit to main menu

def update_category(cursor,db):
    category_id=int(input('Enter the category id= '))
    updated_name=input('Enter the new category name= ').strip().capitalize()
    cursor.execute('update category set name=%s where cid=%s',(updated_name,category_id))
    commit_and_message(cursor,db,"one record updated")
    display_category(cursor,db)
    
    
       
def delete_category(cursor,db):
    category_id=int(input('Enter the category id='))
    cursor.execute('delete from category where cid= %s',(category_id))
    commit_and_message(cursor,db,"one record deleted")
    display_category(cursor,db)
    
    
    
    
def display_category(cursor,db):
    cursor.execute('select * from category')
    result=cursor.fetchall()
    columns=['Category  ID','category Name']
    print(tabulate(result,headers=columns,tablefmt='psql'))
    
    

def category_menu(cursor,db):
    while True:
        print('\n** Category Menu **')
        print('\n1. Add Category')
        print('2. Update Category')
        print('3. Delete Category')
        print('4. Display Category')
        print('5. Exit to main menu ')
        
        
        choice=input('Enter Your Choice= ')
        
        if choice == '1':
            add_category(cursor,db)
            # return # Redirect to main menu after adding a category
        elif choice == '2':
            update_category(cursor,db)
        elif choice == '3':
            delete_category(cursor,db)
        elif choice == '4':
            display_category(cursor,db)
        elif choice == '5':
            break
        else:
            print('Invalid Choice....')  
    
    
    

    
    
    
#______________Products code started_________________________


def add_Product(cursor,db):
    while True:
        Product_name = input('Enter The Product Name = ').capitalize().strip()
        Category_id = int(input('Enter The Category ID = '))
        Price=float(input('Enter The Price of products = '))
        
        #check if the product name is already exist
        cursor.execute('select count(*) from products where name=%s',(Product_name))
        
        if cursor.fetchone()[0] > 0:
            print(f"Product {Product_name} is already exists ")
        else:
            cursor.execute('insert into products(name,category_id,price) values(%s,%s,%s)',(Product_name,Category_id,Price))
            commit_and_message(cursor,db,"Data Inserted Successfully")
            display_product(cursor,db)
            
        result=input('Do you want to add another Product? (yes/no) = ').strip().lower()
        if result == 'no':
            break
            # return

def update_product(cursor,db):
    
    Product_id=int(input('Enter the Product Id = '))
    
    update_name=input('Enter the new Product Name = ').strip().capitalize()
    update_category_id=int(input('Enter the new category_id = '))
    up_price=float(input('Enter the New Price = '))
    
    cursor.execute ('update products set name=%s,category_id=%s,price=%s where pid=%s',(update_name,update_category_id,up_price,Product_id))
    
    commit_and_message(cursor,db,'One record updated')
    display_product(cursor,db)
    
def delete_product(cursor,db):
    
    Product_id=int(input('Enter the Product Id = '))
    
    cursor.execute('delete from products where pid=%s',(Product_id))
    commit_and_message(cursor,db,'One record deleted.')
    display_product(cursor,db)


def display_product(cursor,db):
    cursor.execute('select * from products')
    result=cursor.fetchall()
    columns=['Product ID','Product Name','Category ID','Price']
    print(tabulate(result,headers=columns,tablefmt='psql'))
    

                
def product_menu(cursor,db):
    while True:
        print('\n Products Menu ')
        print('\n1. Add Product')
        print('2. Update Product')
        print('3. Delete Product')
        print('4. Display Products')
        print('5. Exit to main menu ')
        
        
        choice=input('Enter Your Choice= ')
        
        if choice == '1':
            add_Product(cursor,db)
            # return # Redirect to main menu after adding a product
        elif choice == '2':
            update_product(cursor,db)
        elif choice == '3':
            delete_product(cursor,db)
        elif choice == '4':
            display_product(cursor,db)
        elif choice == '5':
            break
        else:
            print('Invalid Choice....')
            
            
            
    
#______________orders code started_________________________


def add_order(cursor,db):
    while True:
        cust_id=input("Enter the Customer Id = ").lower() #ex -- c-1
        cname=input("Customer Name = ").strip().title()
        cid=int(input('Enter the category Id = '))
        pid = int(input('Enter the product Id = '))
        quty=int(input('Enter the number of quty =' ))
        unit_price=float(input('Enter the unit price of product =' ))
        total_bill=quty* unit_price
        order_date=datetime.now()
        
        
        
        cursor.execute("Insert into orders(cust_id,cname,category_id,product_id,qnty,unit_price,total_bill,odate) values(%s,%s,%s,%s,%s,%s,%s,%s)",(cust_id,cname,cid,pid,quty,unit_price,total_bill,order_date))
        
        commit_and_message(cursor,db,'Order placed Successfully')
        result=input('Do you want to add another Order? (yes/no) = ').strip().lower()
        if result == 'no':
            break
        
        
def display_bill(cursor,db):
    cust_id=input('Enter the customer Id= ')
    cursor.execute('select o.cname,o.qnty,o.total_bill,c.name,p.name from orders o join products p on o.product_id = p.pid join category c on o.category_id=c.cid where cust_id = %s',(cust_id))
    
    result=cursor.fetchall()
    columns=['Customer name','Qnty','Total','Category Name','Product Name']
    
    print(tabulate(result,headers=columns,tablefmt='psql'))
    
    



def order_menu(cursor,db):
    while True:
        print("\n Order Menu")
        print(' 1 .Add Order')
        print(' 2 .Display Bill')
        print(' 3 .Exit to main')
        
        choice=input("Enter your choice = ")
        
        if choice == '1':
            add_order(cursor,db)
        elif choice == '2':
            display_bill(cursor,db)
        elif choice == '3':
            break
        else:
            print("Invalid choice")
            
            
        
        
            
    











#___________________________________________________________________________________________________________________________________________________________________
                     



        
            
def main_menu():
    db=connect_db()
    cursor=db.cursor()
    if not login(cursor):
        return
    while True:
        print("\n Main Menu")
        print("\n1. Add Category")
        print("2. Add Products")
        print("3. Add Orders")
        print("4. Exit from main Menu")
        
        choice=input('Enter Your Choice = ')
        
        if choice == '1':
            category_menu(cursor,db)
        elif choice == '2':
            product_menu(cursor,db)
        elif choice == '3':
            order_menu(cursor,db)
        elif choice == '4':
            print('Exiting Program....')
            break
        else:
            print('Enter proper choice')
            
if __name__ == '__main__':
    main_menu()
        