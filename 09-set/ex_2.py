

#  Write a Python program to add member(s) to a set.

#  Write a Python program to remove item(s) from a given set.
#  Write a Python program to remove an item from a set if it is present in the set

# d=set(["a", "b", "c", "d",1251])

# d.add("Murali")
# d.add("Swapnil")

# # # d.remove("a")
# # d.remove("f")

# for i in d:
#     print(i)


demo=set([1,2,3,"murali"])

demo.add("karpe")
demo.update(["Patil","kore","mahadik"])

demo.discard("rane")
demo.remove("murali")
# demo.remove("reme")

for i in demo:
    print(i)