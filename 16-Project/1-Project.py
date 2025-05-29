import pymysql as ss
from tabulate import tabulate
import datetime





def Created_Project():
    print("\n***Personal Information***")
    print("1) Add  information =")
    print("2) Search particular person =")
    print("3) Edit the person=")
    print("4) Delete the person=")
    print("5) Display all  information")
    print("6) Exite....")



    
    
    
    
def add_person(person):
    while True:
        emp_name=input("Enter the name of the Employee:")
        Age=int(input("Enter the age:"))
        email=input("Enter the email:")
        contact=input("Enter the contact:")
        
        try:
            conection=ss.connect(host="localhost",user="root",password="root",database="python_aug_2024")
            
            
            cur=conection.cursor()
            insert_person="insert into emp (name,age,email,contact) values(%s,%s,%s,%s)"
            
            cur.execute(insert_person,(emp_name,Age,email,contact))
            conection.commit()
            print("One Record Inserted",cur.rowcount)
            
        except Exception as err:
            print(err)
    
        more=input("Add another information(yes/no):").lower()
        if more == "no":
            break
        
        
        
def search_person(person):
    
    user_id=int(input("Enter the ID to search :"))
    
    try:
        conn=ss.connect(host="localhost",user="root",password="root",database="python_aug_2024")
        
        
        cur=conn.cursor()
        
        select_person="select * from emp where eid=%s"
        cur.execute(select_person,(user_id))
        
        result=cur.fetchone()
        
        headers=["ID","Name","Age","Email","Contact","created_at","Updated_at"]
        
        if result is None:
            print(f"No records found  !")
        else:
            print(tabulate([result],headers=headers,tablefmt="grid"))
        
        
    
    except Exception as err:
        print(err)
        

        
        
def update_person(person):
    emp_name=input("Enter the name of the Employee:")
    Age=int(input("Enter the age:"))
    email=input("Enter the email:")
    contact=input("Enter the contact:")
    update_at=datetime.datetime.now()
    new_update_at=update_at.strftime("%Y-%m-%d-%H:%M:%S")

    id=int(input("Enter the id to update the data:"))
    
    def dis_update_person():
        try:
            conection=ss.connect(host="localhost",user="root",password="root",database="python_aug_2024")
        
            cur=conection.cursor()
        
            select_person="select * from emp where eid=%s "
        
            cur.execute(select_person,(id,))
            result=cur.fetchone()
        
            
            
            if result :
                headers=["ID","Name","Age","Email","Contact","created_at","Updated_at"]
                print(tabulate([result],headers=headers,tablefmt="grid"))
                
            else:
                print("No record found!")
                
        

    
        except Exception as err:
            print(err)
    
    
    try:
        conection=ss.connect(host="localhost",user="root",password="root",database="python_aug_2024")
            
        cur=conection.cursor()
        check_sql="select * from emp where eid=%s"
        cur.execute(check_sql,(id,))
        
        if cur.rowcount == 0:
            print(f"No record found with ID :{id}")
        else:
            update_person="update emp set name=%s,age=%s,email=%s,contact=%s,updated_at=%s where eid=%s"
            cur.execute(update_person,(emp_name,Age,email,contact,new_update_at,id))
            conection.commit()
            print(cur.rowcount,"record updated successfully")
            dis_update_person()
    except Exception as err:
        print(err)



            
            
    

    
    







def delete_person(person):
    user_id=int(input("Enter the id to delete:"))
    try:
        conn=ss.connect(host="localhost",user="root",password="root",database="python_aug_2024")
        
        cur=conn.cursor()
        
        select_person="select * from emp where eid=%s"
        cur.execute(select_person,(user_id,))
        
        result=cur.fetchall()
        headers=["ID","Name","Age","Email","Contact","created_at","Updated_at"]
        
        if not result:
            print(f"No record found with ID :{user_id}")
        else:
            print(tabulate(result,headers=headers,tablefmt="grid"))
            delete_sql="delete from emp where eid=%s"
            cur.execute(delete_sql,(user_id,))
            conn.commit()
            print(cur.rowcount,"record deleted successfully")
            
            
    except Exception as err:
        print(err)
        
        
        
        
        
def display_allperson(person):
    
    try:
        conn=ss.connect(host="localhost",user="root",password="root",database="python_aug_2024")
        
        cur=conn.cursor()
        
        select_allperson="select * from emp"
        cur.execute(select_allperson)
        
        result=cur.fetchall()
        headers=["ID","Name","Age","Email","Contact","created_at","Updated_at"]
        
        if not result:
            print("Empty record !")
        else:
            print(tabulate(result,headers=headers,tablefmt="grid"))
    
    except Exception as err:
        print(err)
        
        
        
def main():
    person=[]
    
    while True:
        Created_Project()
        choice=int(input("Enter Your choice:"))
        
        if choice == 1:
            add_person(person)
        
        elif choice == 2:
            search_person(person)
        elif choice == 3:
            update_person(person)
        elif choice == 4:
            delete_person(person)
        elif choice == 5:
            display_allperson(person)
        elif choice == 6:
            print("Exiting Program....")
            break
        else:
            print("Invalid Choice....")
            
if __name__ == "__main__":
    main()
    
        
        
        
    
    
       
        
        
    
               

            
    
             
            
            
            
        
    
    


    
    
