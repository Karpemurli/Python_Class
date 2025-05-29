# 2.	How can you find the union of two sets?
my_set={1,2,3,4,5,6,7,8}
my_set2=set([11,12,13,14,15,16,17])


# union_set=my_set.union(my_set2)
union_set=my_set | my_set2

print("Union of two sets:",union_set)
