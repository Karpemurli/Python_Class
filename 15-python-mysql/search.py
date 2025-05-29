#searching the id vice

import pymysql as ms

from tabulate import tabulate

user_id=int(input("Enter the id to search="))

try:
    conn=ms.connect(host="localhost",user="root",password="root",database="python_aug_2024")
    
    
    cur=conn.cursor()
    select_sql="select * from info where id=%s"
    cur.execute(select_sql,(user_id))
    
    # result=cur.fetchall()#this method retrive all the data from table
    result=cur.fetchone()  #display one record.
    
  
    
    headers=["ID","Student_name","Age","City","Created_At","Updated_At"]
    
    if result is None:  #CHECK IF RESULT IS EMPTY.
        print("The ID  Does not exist in the database.")
    else:
        print(tabulate([result],headers=headers,tablefmt="grid"))


except Exception as err:
    print(err)

