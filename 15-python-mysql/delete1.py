#delete the name vice

import pymysql as ms

from tabulate import tabulate

user_name=input("Enter the name to Delete=")

try:
    conn=ms.connect(host="localhost",user="root",password="root",database="python_aug_2024")
    
    
    cur=conn.cursor()
    select_sql="select * from info where name=%s"
    cur.execute(select_sql,(user_name))
    
    result=cur.fetchall()#this method retrive all the data from table
    
    if result:
        headers=["ID","Student_name","Age","City","Created_At"]
        print(tabulate(result,headers=headers,tablefmt="grid"))
        print("Record to be deleted !")
    else:
        
        print(f"No record found= {user_name}")
    
    delete_sql="delete from info where name=%s"
    cur.execute(delete_sql,(user_name))
    conn.commit()
    

except Exception as err:
    print(err)


