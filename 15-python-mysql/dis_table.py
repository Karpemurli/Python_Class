import pymysql as ms

from tabulate import tabulate

try:
    conn=ms.connect(host="localhost",user="root",password="root",database="python_aug_2024")
    
    if conn:
        print("Connected to MySQL server")
    cur=conn.cursor()
    select_sql="select * from info"
    cur.execute(select_sql)
    
    result=cur.fetchall()#this method retrive all the data from table
    
    # for row in result:
    #     print(row)
    
    headers=["ID","Student_name","Age","City","Created_At"]
    print(tabulate(result,headers=headers,tablefmt="grid"))


except Exception as err:
    print(err)