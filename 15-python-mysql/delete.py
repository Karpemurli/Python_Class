# #delete the id vice

import pymysql as ms

from tabulate import tabulate

user_id=int(input("Enter the id to delete:"))

try:
    conee=ms.connect(host="localhost",user="root",password="root",database="python_aug_2024")
    
    cur=conee.cursor()
    
    select_sql="select * from info where id=%s"
    cur.execute(select_sql,(user_id,))
    result=cur.fetchall()
    
    headers=["ID","Student_name","Age","city","created_at"]
    
    if not result:
        print(f"record not found: {user_id}")
    else:
        print(tabulate(result,headers=headers,tablefmt="grid"))
        
    
    
        delete_sql="delete from info where id=%s"
        cur.execute(delete_sql,(user_id,))
        conee.commit()
        print(f"record to be {user_id} deleted")
except Exception as err:
    print(f"Error: {err}")
    

