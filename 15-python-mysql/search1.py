

# #searching the name vice

import pymysql as ms

from tabulate import tabulate

user_name=input("Enter the name to search=")

try:
    conn=ms.connect(host="localhost",user="root",password="root",database="python_aug_2024")
    
    
    cur=conn.cursor()
    select_sql="select * from info where name=%s"
    cur.execute(select_sql,(user_name))
    
    # result=cur.fetchall()#this method retrive all the data from table
    result=cur.fetchone()
    

    
  
    
    headers=["ID","Student_name","Age","City","Created_At","Updated_At"]
    if result is None:
        print("No record found!")
    else:
        print(tabulate([result],headers=headers,tablefmt="grid"))


except Exception as err:
    print(err)





# #searching the city vice
# user_city=input("Enter the city to search=")

# try:
#     conn=ms.connect(host="localhost",user="root",password="root",database="python_aug_2024")
    
    
#     cur=conn.cursor()
#     select_sql="select * from info where city=%s"
#     cur.execute(select_sql,(user_city))
    
#     result=cur.fetchall()#this method retrive all the data from table
    
  
    
#     headers=["ID","Student_name","Age","City","Created_At"]
#     print(tabulate(result,headers=headers,tablefmt="grid"))


# except Exception as err:
#     print(err)