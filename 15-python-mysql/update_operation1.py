
#update zalela data display karane.

import pymysql as ss 
from tabulate import tabulate



stud_name=input("Enter the name:")
age=int(input("Enter the age:"))
city=input("Enter the city:")

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
    
        if result:
            headers=["ID","Student_name","Age","City","Created_At"]
            print(tabulate([result],headers=headers,tablefmt="grid"))
        else:
            print("No record found!")


    except Exception as err:
      print(err)
    


try:
    conn=ss.connect(host="localhost",user="root",password="root",database="python_aug_2024")
    
    if conn:
        print("Connected to MySQL server")
    
    cur=conn.cursor()
    update_sql="update info set name=%s,age=%s,city=%s where id=%s"
    
    cur.execute(update_sql,(stud_name,age,city,id))
    conn.commit()
    
    print(cur.rowcount,"record updated successfully")
    displayData()
    
except Exception as err:
    print(f"Error: {err}")    