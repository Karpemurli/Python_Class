

#finally: keyword :excception ala tari keyword always run hoto..


marks=100
try:
    res=marks/0
    print(res)
except ZeroDivisionError as err: 
    print(err)

finally:
    print("This block will always run.")