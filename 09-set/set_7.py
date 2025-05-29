# Intersection update() method

# s1={1,2,3,4}
# s2={5,6,2,3}

# s3=s1.intersection(s2)   using intersection ans={2, 3}
# print(s3)


s1={1,2,3,4,5,7}
s2={3,4,5,6,7}
s1.intersection_update(s2) #Intersection update() method
print(s1)


s1={1,2,3,4,5}
s2={3,4,5,6,7}
s3={}             # original set remove elements

s3=s1.intersection_update(s2) #Intersection update() method
print(s3)
