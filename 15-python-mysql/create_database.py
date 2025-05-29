import pymysql as msql

try:
    connection=msql.connect(host="localhost",user="root",password="root")
    if connection:
        print("connected")
        
        
    cur=connection.cursor() #here  we define the cursor
    cur.execute("create database if not exists  python_aug_2024")
    print("Database created.")


except Exception as err:
    print(err)