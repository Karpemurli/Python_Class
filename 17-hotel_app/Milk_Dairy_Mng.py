import pymysql as ss
from dotenv import load_dotenv
import os
from tabulate import tabulate
from datetime import datetime
import pyautogui



load_dotenv()
my_password=os.getenv('db_pass')
 
# print(my_password)

def connect_db():
    return ss.connect(host='localhost',user='root',passwd=my_password,database='milk_dairy')

def commit_message(cursor,db,message):
    db.commit()
    print(message)
    
    
#______________________________ Login ____________________________________

def login(cursor):
    while True:
        uname=input('\nEnter the username = ').strip()
        upass=pyautogui.password(text='Enter the user password :',title= 'Enter Password',default= '',mask='*')
        
        cursor.execute('select * from users where username=%s and password=%s',(uname,upass))
        
        user=cursor.fetchone()
        
        if user:
            print('Login Successful = ' , uname)
            return True
        else:
            print('Invalid username or password please check again .....')
            


#__________________________ Farmer Management _________________________________


def add_farmer(cursor,db):
    while True:
        name=input('\nEnter the Name = ').title().strip()
        phone=input('Enter the Contact = ').strip()
        address=input('Enter the Address = ').title().strip()
        
        cursor.execute('insert into farmer(name, phone, address)values(%s,%s,%s)',(name,phone,address))
        commit_message(cursor,db, '\n Data Inserted successfully')
        view_farmers(cursor,db)
        
        result=input('Do you want to add another farmer? (yes/no): ').strip().lower()
        
        if result  == 'no':
            break
        
def update_farmer(cursor,db):
    
    farmer_id=int(input('\nEnter the Farmer Id = '))
    
    name=input('Enter the new name: ').title().strip()
    phone=input('Enter the new phone: ').strip()
    address=input('Enter the new address: ').title().strip()
    
    cursor.execute('update farmer set name=%s, phone=%s, address=%s where f_id=%s',(name,phone,address,farmer_id))
    
    commit_message(cursor,db, '\n Data Updated successfully')
    
    cursor.execute('select * from farmer where f_id=%s',(farmer_id,))
    result=cursor.fetchone()
    
    if result:
        columns=['Farmer_ID','Farmer_Name','Contact','Address']
        print(tabulate([result],headers=columns,tablefmt='psql'))  
    else:
        print('\n No Farmer Found with the Given ID.')
        
        
def delete_farmer(cursor,db):
    farmer_id=int(input('\nEnter the Farmer ID = '))
    
    cursor.execute('delete from farmer where f_id=%s',(farmer_id)) 
    commit_message(cursor,db, '\n Data Deleted successfully.')
    view_farmers(cursor,db)   
        
        
def view_farmers(cursor,db):
    cursor.execute('select * from farmer')
    result=cursor.fetchall()
    
    columns=['Farmer_ID','Farmer_Name','Contact','Address']
    print(tabulate(result,headers=columns,tablefmt='psql'))
    
    
def farmer_menu(cursor,db):
    while True:
        print('\n ** Farmer Management **')
        print(' 1. Add Farmer')
        print(' 2. Update Farmer')
        print(' 3. Delete Farmer')
        print(' 4. Display Farmers')
        print(' 5. Exit Main Menu')
        
        choice=input('\n Enter Your Choice = ')
        
        if choice == '1':
            add_farmer(cursor,db)
        elif choice == '2':
            update_farmer(cursor,db)
        elif choice == '3':
            delete_farmer(cursor,db)
        elif choice == '4':
            view_farmers(cursor,db)
        elif choice == '5':
            break
        else:
            print('\n Invalid Choice....')
            
            
#____________________________________________________ Milk Collection _________________________________________-

def add_milk_collection(cursor,db):
    
    while True:
    
        farmer_id  =int(input('Enter the Farmer Id : '))
        date_time=datetime.now()
        Quantity=float(input('Enter the Quantity : '))
        Fat_content=float(input('Enter the Fat Content : '))
        Price_per_liter=float(input('Enter the Price_per_liter : '))
        Total_price=Quantity*Price_per_liter
        
        cursor.execute('insert into milkcollection (farmer_id,datetime,quantity,fat_content,price_per_liter,total_price) values(%s,%s,%s,%s,%s,%s)',(farmer_id,date_time,Quantity,Fat_content,Price_per_liter,Total_price))
        commit_message(cursor,db,'Data inserted Successfully')
        view_milk_collection(cursor,db)
        
        result=input('Do you want to add another? (yes/no):  ').strip().lower()
        
        if result == 'no':
            break
        
def update_milk_collection(cursor,db):
    Collation_id=input('Enter Your New Collation ID = ')
    
    farmer_id  =int(input('Enter the New Farmer Id : '))
    date_time=datetime.now()
    new_datetime=date_time.strftime("%Y-%m-%d-%H:%M:%S")
    Quantity=float(input('Enter the New Quantity : '))
    Fat_content=float(input('Enter the New Fat Content : '))
    Price_per_liter=float(input('Enter the New Price_per_liter : '))
    Total_price=Quantity*Price_per_liter
    
    cursor.execute('update milkcollection set farmer_id=%s, datetime=%s,quantity=%s,fat_content=%s,price_per_liter=%s,total_price=%s where c_id=%s',(farmer_id,new_datetime,Quantity,Fat_content,Price_per_liter,Total_price,Collation_id))
    
    commit_message(cursor,db,'Data Updated Successfully')
    
    cursor.execute('select * from milkcollection where c_id=%s',(Collation_id,))
    
    result=cursor.fetchone()
    
    
    if result:
        columns=['Collation_id','Farmer Id','Datetime', 'Quantity', 'Fat_content', 'Price_per_liter', 'total_price']
        print(tabulate([result],headers=columns,tablefmt='psql'))
        
    else:
        print('\n No Collection Found with the Given ID.')
        



def delete_milk_collection(cursor,db):
    
    Collation_id=int(input('Enter the Collection ID = '))
    
    cursor.execute('delete from milkcollection where c_id=%s',(Collation_id,))
    
    commit_message=(cursor,db,'\n Data Deleted successfully.')
    
    view_milk_collection(cursor,db)
    
    
def view_milk_collection(cursor,db):
    
    cursor.execute('select * from milkcollection')
    
    
    result=cursor.fetchall()
    
    columns=['Collation_id','Farmer Id','Datetime', 'Quantity', 'Fat_content', 'Price_per_liter', 'total_price']
    print(tabulate(result,headers=columns,tablefmt='psql'))
    
    
def milk_collection_menu(cursor,db):
        while True:
            print('\n **  Milk Collection **')
            print('\n 1. Add Collection')
            print(' 2. Update Collection')
            print(' 3. Delete Collection')
            print(' 4. Display Collection')
            print(' 5. Exit Main Menu')
            
            choice=input('\n Enter Your Choice = ')
            
            if choice == '1':
                add_milk_collection(cursor,db)
            elif choice == '2':
                update_milk_collection(cursor,db)
            elif choice == '3':
                delete_milk_collection(cursor,db)
            elif choice == '4':
                view_milk_collection(cursor,db)
            elif choice == '5':
                break
            else:
                print('\n Invalid Choice....')
                

#___________________________________________ Customer Management _______________________________________


def add_Customer_mng(cursor,db):
    
    while True:
    
        name=input('Enter the name of the customer = ').title().strip()
        phone=input('Enter the phone number = ')
        address=input('Enter the address = ').title().strip()
        
        cursor.execute('insert into customer (name,phone,address) values(%s,%s,%s)',(name,phone,address))
        
        commit_message(cursor,db,' Data inserted successfully')
        view_customer(cursor,db)
        result=input('Do you want to add another? (yes/no): ').strip().lower()
        
        if result == 'no':
            break
        
def update_customer(cursor,db):
    
    customer_id=int(input('Enter the Customer ID: '))
    
    name=input('Enter the New name of the customer = ').title().strip()
    phone=input('Enter the New phone number = ')
    address=input('Enter the New address = ').title().strip()
    
    cursor.execute('update customer set name=%s, phone=%s, address=%s where c_id=%s',(name,phone,address,customer_id))
    
    commit_message(cursor,db,'Record Update Successfully')
    
    cursor.execute('select * from customer where c_id=%s',(customer_id,))
    result=cursor.fetchone()
    
    
    if result:
        columns=['customer_id','Name','Phone','Address']
        print(tabulate([result],headers=columns,tablefmt='psql'))
    else:
        print('\n No Collection Found with the Given ID.')
    
    
    
def delete_customer(cursor,db):
    
    customer_id=int(input('Enter Customer ID: '))
    
    cursor.execute('delete from customer where c_id = %s',(customer_id))
    
    commit_message(cursor,db,' Data deleted successfully')
    view_customer(cursor,db)
    
def view_customer(cursor,db):
    
    cursor.execute('select * from customer')
    result=cursor.fetchall()
    
    columns=['Customer_ID','Customer_Name','Phone','Address']
    print(tabulate(result,headers=columns,tablefmt='psql'))
    
    


def customer_menu(cursor,db):
    while True:
        print('\n ** Customer Management **')
        print('\n 1. Add Customer')
        print(' 2. Update Customer')
        print(' 3. Delete Customer')
        print(' 4. Display Customer')
        print(' 5. Exit Main Menu')
            
        choice=input('\n Enter Your Choice = ')
            
        if choice == '1':
            add_Customer_mng(cursor,db)
        elif choice == '2':
            update_customer(cursor,db)
        elif choice == '3':
            delete_customer(cursor,db)
        elif choice == '4':
            view_customer(cursor,db)
        elif choice == '5':
                break
        else:
                print('\n Invalid Choice....')
        
        
#___________________________________ Milk Sales _______________________________________


def add_milk_sales(cursor,db):
    while True:
    
        customer_id=int(input('Enter the Customer ID :  '))
        date_time=datetime.now()
        Quantity=float(input('Enter the Quantity : '))
        Price_per_liter=float(input('Enter the Price Perliter : '))
        Total_price=Quantity*Price_per_liter
        
        cursor.execute('insert into milksales (customer_id,datetime,quantity,price_per_liter,total_price) values(%s,%s,%s,%s,%s)',(customer_id,date_time,Quantity,Price_per_liter,Total_price))
        commit_message(cursor,db,'Data inserted successfully')
        
        view_milk_sales(cursor,db)
        
        result=input('Do you want to add another? (yes/no):').lower().strip()
        
        if result == 'no':
            break
        
        
    
    
    
    
    
def update_milk_sales(cursor,db):
    sales_id=int(input('Enter the Milk Sales ID = '))
    
    customer_id=int(input('Enter the Customer ID :  '))
    date_time=datetime.now()
    newdatetime=date_time.strftime('%Y-%m-%d %H:%M:%S')
    Quantity=float(input('Enter the Quantity : '))
    Price_per_liter=float(input('Enter the Price Perliter : '))
    Total_price=Quantity*Price_per_liter
    
    cursor.execute('update milksales set customer_id=%s,datetime=%s,quantity=%s,price_per_liter=%s,total_price=%s where s_id=%s',(customer_id,newdatetime,Quantity,Price_per_liter,Total_price,sales_id))
    
    commit_message(cursor,db,'record Updated successfully')
    
    cursor.execute('select * from milksales where s_id=%s ',(sales_id,))
    
    result=cursor.fetchone()
    
    if result:
        columns=['Milksales_ID','Customer Id','Datetime','Quantity','Price_per_liter','Total']
        print(tabulate([result],headers=columns,tablefmt='psql'))
    else:
        print('\n No  Found with the Given ID.')
    
    

def delete_milk_sales(cursor,db):
    
    sales_id=int(input('Enter the Milk Sales ID = '))
    cursor.execute('delete from milksales where s_id=%s',(sales_id,))
    commit_message(cursor,db,'Data deleted successfully')
    view_milk_sales(cursor,db)
    
def view_milk_sales(cursor,db):
    
    cursor.execute('select * from milksales')
    result=cursor.fetchall()
    
    
    columns=['Milksales ID','customer Id','Datetime','Quantity','Price_per_liter','Total_price']
    print(tabulate(result,headers=columns,tablefmt='psql'))
    
    
def milk_sales_menu(cursor,db):
    while True:
        print('\n ** Milk Sales **')
        print(' 1.Add Milk Sales')
        print(' 2.Update Milk Sales')
        print(' 3.Delete Milk Sales')
        print(' 4.Display Milk Sales')
        print(' 5.Exit Main Menu')
        
        choice=input('\nEnter Your Choice = ')
        
        if choice == '1':
            add_milk_sales(cursor,db)
        elif choice == '2':
            update_milk_sales(cursor,db)
        elif choice == '3':
            delete_milk_sales(cursor,db)
        elif choice == '4':
            view_milk_sales(cursor,db)
        elif choice == '5':
            break
        else:
            print('\n Invalid Choice.... ')
            
#__________________________________________ Farmer Payment _________________________________________


def farmer_bill(cursor,db):
    pass
    
def update_bill(cursor,db):
    pass
    
def pay_bill(cursor,db):
    pass
    
def view_bills(cursor,db):
    pass
    


def farmer_payment(cursor,db):
    while True:
        print('\n ** Farmer Payment **')
        print('')
           
                
        
            
        
            
            
    
    
        
    
    
    
            
            
            
#_______________________ main menu ________________________________________


def main_menu():
    db=connect_db()
    cursor=db.cursor()
    
    if not login(cursor):
        return
    while True:
        print('\n ** Milk Dairy Management System **')
        print('\n 1. Farmer Management ')
        print(' 2. Milk Collection')
        print(' 3. Customer Management')
        print(' 4. Milk Sales ')
        print(' 5. Farmer Payment')
        print(' 6. Customer_bill')
        print(' 7. Exit Main Page')
        
        
        choice=input('\nEnter Your Choice = ')
        
        if choice == '1':
            farmer_menu(cursor,db)
        elif choice == '2':
            milk_collection_menu(cursor,db)
        elif choice == '3':
            customer_menu(cursor,db)
        elif choice == '4':
            milk_sales_menu(cursor,db)
        elif choice == '5':
            print('Farmer Payment')
        elif choice == '6':
            print('Customer_bill')
        elif choice == '7':
            print('Exiting Program....')
            commit_message(cursor,db,'Program exited')
            break
        else:
            print('Enter Proper Choice....')
            


if __name__ == '__main__':
    main_menu()
        
            
        
    
    