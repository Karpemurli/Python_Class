import pymysql as ms


try:
    conn=ms.connect(host="localhost",user="root",password="root",database="python_aug_2024")
    if conn:
        print("Connected to MySQL server")
    cur=conn.cursor()
    create_table_info="""
    create table info(id int(5) primary key auto_increment,name varchar(30),age int,city varchar(30),created_at timestamp default 
    current_timestamp)
    """
    cur.execute(create_table_info)
    print("Table created successfully")


except Exception as err:
    print(f"Error: {err}")