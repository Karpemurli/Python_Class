# # Self: Pointer to the Current Object
# class check:
#     def __init__(self):
#         print("Address of self = ",id(self))
        
# obj = check()
# print("Address of self = ",id(obj))



# Class and Instance Attributes in Python


class sampleclass:
    count= 0
    
    
    def increase(self):
        sampleclass.count += 1
        
s1 = sampleclass()
s1.increase()
print(s1.count)


s2 = sampleclass()
s2.increase()
print(s2.count)

print(sampleclass.count)