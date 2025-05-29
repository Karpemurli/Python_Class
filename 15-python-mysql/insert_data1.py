

#user throw add multiple data in table.

import pymysql as ss

while True:
    Student_name=input("Enter the name=")
    Age=int(input("Enter the age="))
    city=input("Enter the city=")

    try:
        connection=ss.connect(host="localhost",user="root",password="root",database="python_aug_2024")
    
        if connection:
           print("connected")
        
        cur=connection.cursor()
        insert_sql="insert into info(name,age,city) values(%s,%s,%s)"
        cur.execute(insert_sql,(Student_name,Age,city))
        connection.commit() #by using commit we can save the data permannantly into table.
        print("One record inserted",cur.rowcount)


    except Exception as e:
      print(e)
      
    more=input("More information add(yes/no):")
    if more == "no":
        break
      
    

    
    