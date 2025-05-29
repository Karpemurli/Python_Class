# Question 3: Remove Duplicates from a Tuple
# Write a Python program that does the following:
# 1.	Accepts a tuple of integers from the user.
# 2.	Converts it into a set to remove duplicates.
# 3.	Converts it back into a sorted tuple.
# 4.	Prints the original and the modified tuple.

user=input("Enter a tuple of integeres:").split()

input_tuple=tuple(map(int,user))

modified_tuple=tuple(sorted(set(input_tuple)))

print("Original Tuple:", input_tuple)
print("Modified Tuple:", modified_tuple)