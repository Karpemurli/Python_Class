# keyword based argument


# def person(**data):
#     for key,value in data.items():
#         print("{} is {}".format(key, value))
        
        
# person(Firstname="murali" ,Lastname="Karpe" )
# person(Firstname="swapnil",Lastname="Karpe")

def person(**data):
    for key,value in data.items():
        print("{} is {}".format(key, value))
        
        
person(Firstname="murali" ,Lastname="Karpe",phone=9850553870 )
