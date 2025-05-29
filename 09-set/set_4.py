

# months=set(["Jan", "Feb"])
# months.update(["Mar", "Apr", "May"])
# months.discard("DEc")                    #discard


# for i in months:
#     print(i)
    
    
# months=set(["Jan", "Feb"])
# months.update(["Mar", "Apr", "May"])
# months.remove("Dec")                 #remove  KeyError: 'Dec'


# for i in months:
#     print(i)



# months.clear()
# print(months)  # clear  all elements removed 


my_set = {1, 2, 3}

# my_set.remove(2)  # Set becomes {1, 3}

# my_set.discard(4)  # No error raised, set remains {1, 3}

my_set.remove(4)  # KeyError raised

print(my_set)