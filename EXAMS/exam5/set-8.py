# 8.	How can you check if one set is a subset of another?


set1={1,2,3}
set2=set([1,2,3,4,5,])

sub_set=set1.issubset(set2)
# sub_set=set2.issubset(set1)

print(f"Subset = ",sub_set)