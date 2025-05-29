import pymysql as ss

try:
    conn=ss.connect(host="localhost",user="root",password="root",database="python_aug_2024")
    
    if conn:
        print("Connecting successfully")
        
        
    cur=conn.cursor()
    create_table_emp="""
    create table emp(eid int(5) primary key auto_increment,name varchar(30),age int,email varchar(30),contact varchar(30),created_at timestamp default current_timestamp)
    
    
    """
    cur.execute(create_table_emp)
    print("Table emp created successfully")

except Exception as err:
    print(err)
