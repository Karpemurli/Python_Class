

dct1 = {"Name":"Murali","age":23,"City":["kolhapur","Pune","satara"]}
print(dct1)

# print(dct1.keys())#dict_keys(['Name', 'age', 'City'])
# print(dct1.values())#dict_values(['Murali', 23, ['kolhapur', 'Pune', 'satara']])


# for x in dct1:
#     print(x) #only keys print
    
# print("The value are:")
# for y in dct1:   #only values print
#     print(dct1[y])


for x,y in dct1.items():
    print(x,"=",y)
   