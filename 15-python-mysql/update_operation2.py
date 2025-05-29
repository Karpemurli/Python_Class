# update the data and display current date-time change and display.


import pymysql as ss 
from tabulate import tabulate
import datetime


stud_name=input("Enter the name:")
age=int(input("Enter the age:"))
city=input("Enter the city:")
updated_at=datetime.datetime.now()
new_updated_at=updated_at.strftime("%Y-%m-%d-%H:%M:%S")  

id=int(input("Enter the id to update the data:"))



def displayData():
    
    try:
        conn=ss.connect(host="localhost",user="root",password="root",database="python_aug_2024")
    
        if conn:
          print("Connected to MySQL server")
        cur=conn.cursor()
        select_sql="select * from info where id=%s"
        cur.execute(select_sql,(id,))
    
        result=cur.fetchone()#this method retrive all the data from table
        # result=cur.fetchall()#this method retrive all the data from table
    
   
    
        headers=["ID","Student_name","Age","City","Created_At"]
        print(tabulate([result],headers=headers,tablefmt="grid"))


    except Exception as err:
      print(err)
    


try:
    conn=ss.connect(host="localhost",user="root",password="root",database="python_aug_2024")
    
    
    
    cur=conn.cursor()
    check_sql="select * from info where id=%s"
    cur.execute(check_sql,(id,))
    
    if cur.rowcount == 0:
        print(f"No record found with ID :{id}")
    else:
        update_sql="update info set name=%s,age=%s,city=%s,updated_at=%s where id=%s"
        cur.execute(update_sql,(stud_name,age,city,new_updated_at,id))
        conn.commit()
    
        print(cur.rowcount,"record updated successfully")
        displayData()
    
except Exception as err:
    print(f"Error: {err}")    


