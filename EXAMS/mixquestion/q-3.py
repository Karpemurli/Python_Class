
# 43.	Explain the difference between shallow copy and deep copy in Python.

import copy


#shallow copy

# original_list=[[1,2,3],[4,5,6]]

# shallow_copy=copy.copy(original_list)

# shallow_copy[0][0]=100

# print("Original list:",original_list)  #Original list: [[100, 2, 3], [4, 5, 6]]
# print("Shallow copy:",shallow_copy)    #Shallow copy: [[100, 2, 3], [4, 5, 6]]

#Deep copy

# org=[[1,2,3],[4,5,6]]

# deep_copy=copy.deepcopy(org)

# deep_copy[0][0]=100

# print("Original list:",org)   #Original list: [[1, 2, 3], [4, 5, 6]]
# print("deep copy:",deep_copy) #deep copy: [[100, 2, 3], [4, 5, 6]]


