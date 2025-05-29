#by using add method()


months=set(["Jan", "Feb", "Mar", "Apr", "May",])
# months.add("Dec")#single element add
# for i in months:
#     print(i)
    
    
# #by using update method()
months=set(["Jan", "Feb"])
months.update(["Mar", "Apr", "May"])  #multiple elements update


for i in months:
    print(i)