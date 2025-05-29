import pymysql as ss
from tabulate import tabulate


# #create database connection

# def create_database():
#     try:
#         coneection=ss.connect(host="localhost",user="root",password="root")
#         if coneection:
#           print("Connected to MySQL server")
    
    
#      # Create a cursor object
#         cur=coneection.cursor()
#         cur.execute("create database if not exists midc")
#         print("Created database 'midc")
    
#         cur.close()
#         coneection.close()
#     except Exception as err:
#         print(err)



#-------------------------------------------------------------------------
#-------------------------------------------------------------------------

# #create table

# def create_table():
#     try:
#        conn=ss.connect(host="localhost",user="root",password="root",database="midc")
#        if conn:
#           print("Connected to MySQL server")
    
#        cur=conn.cursor()
#        create_table_emp="""
#        create table emp(eid int primary key auto_increment,name varchar(25),age int,contact varchar(15) )
    
#         """
#        cur.execute(create_table_emp)
#        print("Table emp created successfully")
#        cur.close()
#        conn.close()
#     except Exception as err:
#       print(err)



#-------------------------------------------------------------------------
#-------------------------------------------------------------------------

def basic_operations():
    print("\n Basic Employee operations: ")
    print("\n 1)Add Information: ")
    print(" 2)Search particular person: ")
    print(" 3)Update person: ")
    print(" 4)Delete person: ")
    print(" 5)Display all information: ")
    print(" 6)Exit...")
    

# insert information into table

def insert_table(member):
    while True:
        name=input("\nEnter name: ")
        age=input("Enter age: ")
        contact=input("Enter contact: ")
    
    
        try: 
            conn=ss.connect(host="localhost",user="root",password="root",database="midc")
    
            cur=conn.cursor()
            insert_data="insert into emp (name,age,contact) values(%s,%s,%s)"
    
            cur.execute(insert_data,(name,age,contact))
            conn.commit()  #by using commit we can save the data permannantly into table.
            print("One record inserted",cur.rowcount)
    
        except Exception as err:
            print(err)
    
        more=input("enter the anyone data(yes/no): ").lower()
    
        if more =="no":
          break





# -------------------------------------------------------------------------
# -------------------------------------------------------------------------


# searching the ID 

def search(member):
    user_id=int(input("\nEnter the Id to search to perticulare person: "))
    
    try:
        conn=ss.connect(host="127.0.0.1",user="root",password="root",database="midc")
        
        cur=conn.cursor()
        
        search_id="select * from emp where eid=%s"
        
        cur.execute(search_id,(user_id))
        
        result=cur.fetchone()
        
        
        headers=["ID","Name","Age","Contact"]
        
        if result is None:
            print(f"No records found with ID :{user_id}")
        else:
            print(tabulate([result],headers=headers,tablefmt="psql"))
        
        
        cur.close()
        conn.close()
    
    
    except Exception as err:
        print(err)
        





# -------------------------------------------------------------------------
# -------------------------------------------------------------------------


# Display all tables

def display_tables(member):
    
    try:
        conn=ss.connect(host='127.0.0.1',user='root',password='root',database='midc')
        
        cur=conn.cursor()
        select_all_table="select * from emp"
        
        cur.execute(select_all_table)
        
        result=cur.fetchall()
        
        headers=["ID","Name","Age","Contact"]
        
        if result is None:
            print("No records found!")
        else:
            print(tabulate(result,headers=headers,tablefmt="psql"))
            
        cur.close()
        conn.close()
        
    except Exception as er:
        print(er)
        
       


# -------------------------------------------------------------------------
# -------------------------------------------------------------------------


# updating the data

def update_data(member):
    
    name=input("\nEnter New Name: ")
    Age=int(input("Enter Age: "))
    contact=input("Enter Contact: ")
    
    id=int(input("Enter the id :"))
    
    def update():
        try:
            conn=ss.connect(host="localhost",user="root",password="root",database="midc")
            
            cur=conn.cursor()
            select_data="select * from emp where eid=%s"
            
            
            cur.execute(select_data,(id,))
            
            result=cur.fetchone()
            
            if result:
                headers=["ID","Name","Age","Contact"]
                print(tabulate([result],headers=headers,tablefmt="psql"))
            else:
                print("No records found with ID :",id)
            
                
            
        except Exception as err:
            print(err)
        
        cur.close()
        conn.close()
    
    try:
        conn=ss.connect(host="localhost",user="root",password="root",database="midc")
        
        cur=conn.cursor()
        
        updatedt="update emp set name=%s,age=%s,contact=%s where eid=%s"
        
        
        cur.execute(updatedt,(name,Age,contact,id))
        conn.commit()
        
        if cur.rowcount > 0:
            print(cur.rowcount,"record update success !.")
            update()
        else:
            print("No records found with ID :",id)
        
        cur.close()
        conn.close()
        
    except Exception as err:
        print(err)

# -------------------------------------------------------------------------
# -------------------------------------------------------------------------

#delete record


def delete_record(member):
    
    user_id=int(input("\nEnter user ID for delete: "))
    
    try:
        conn=ss.connect(host="localhost",user="root",password="root",database="midc")
        
        cur=conn.cursor()
        
        select_user="select * from emp where eid=%s"
        
        cur.execute(select_user,(user_id,))
        
        result = cur.fetchone()
        
        
        if result:
            headers=["ID","Name","Age","Contact"]
            print(tabulate([result],headers=headers,tablefmt="psql"))
            print("record delete successful !!")
        else:
            print("No records found =",user_id)
            
        delete_rec="delete from emp where eid=%s"
        
        cur.execute(delete_rec,(user_id))
        conn.commit()
        
    except Exception as err:
        print(err)
        
 
 
 
# create_database()
# create_table()
# insert_table()
# search()
# display_tables()
# update_data()
# delete_record()



def main():
    
    member=[]
    
    
    while True:
        basic_operations()
        choice=int(input("\nEnter Your Choice:  "))
        
        
        if choice == 1:
            insert_table(member)
        elif choice == 2:
            search(member)
        elif choice == 3:
            update_data(member)
        elif choice == 4:
            delete_record(member)
        elif choice == 5:
            display_tables(member)
        elif choice == 6:
            print("\n Exiting Program...")
            break
        else:
            print("Invalid Choice...")
    
if __name__ == "__main__":
    main()
            
    
    





