import pymysql as murali

try:
    conn=murali.connect(host="localhost",user="root",password="root")
    if conn:
        print("Connected to MySQL server")
    cur=conn.cursor()
    cur.execute("Create database if not exists practice")
    print("Created database")
except Exception as err:
    print("Error connecting to MySQL server",err)