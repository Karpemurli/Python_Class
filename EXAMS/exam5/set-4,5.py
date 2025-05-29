# 4.	How can you find the difference between two sets?
# 5.	Write a program to find the symmetric difference of two sets.



set1={1,2,3,4,5,6,7,8,9,10}

set2=set([1,2,3,4,5,6,7])


#difference

# difference_set=set1.difference(set2)
difference_set=set1 - set2
print("Difference of set1 and set2:",difference_set)

#symmetric difference

# symme_set=set1.symmetric_difference(set2)
symme_set=set1 ^ set2

print("Symmetric difference of set1 and set2:",symme_set)
