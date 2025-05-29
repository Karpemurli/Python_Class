#symmetric difference set



# set1=set([1,2,3,4,5,6])
# set2={1,2,9,8,10}

# # set3=set1.symmetric_difference(set2)
# set3=set1 ^ set2

# for i in set3:
#     print(i)


set1=set(["murali","swapnil","karpe","raj"])

set2=set(["murali","swapnil","rohan","harsh"])

set3=set1.symmetric_difference(set2)

# print(set3) #{'raj', 'harsh', 'karpe', 'rohan'}

set4=set2 ^ set1

for i in set4, set3:
    print(i)