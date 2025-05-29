#  Write a Python program to create an intersection of sets


# mla=set(["rai","east","danish",125,55,44])

# mnc=set(["gildline","east","mv9"])

# print(mla.intersection(mnc))

# print(mla & mnc)

# demo=mla.intersection(mnc)

# for i in demo:
#     print(i)



set1=set(["rai","east","danish"])

set2={101,102,103,"rai","east"}


print(set2.intersection(set1))

set3=set1 & set2

print(set3)
set4=set1.intersection(set2)


for i in set4:
    print(i)