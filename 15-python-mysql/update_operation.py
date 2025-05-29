
# data update karane.
import pymysql as ss 




stud_name=input("Enter the name:")
age=int(input("Enter the age:"))
city=input("Enter the city:")
id=int(input("Enter the id to update the data:"))


try:
    conn=ss.connect(host="localhost",user="root",password="root",database="python_aug_2024")
    
    if conn:
        print("Connected to MySQL server")
    
    cur=conn.cursor()
    update_sql="update info set name=%s,age=%s,city=%s where id=%s"
    
    cur.execute(update_sql,(stud_name,age,city,id))
    conn.commit()
    
    print(cur.rowcount,"record updated successfully")
    
except Exception as err:
    print(f"Error: {err}")    