# Write a Python program to split a multi-line string into a list of lines.
# Sample Output:
# Original string: This
# is a
# multiline
# string.
# Split the said multiline string into a list of lines:
# ['This', 'is a', 'multiline', 'string.', '']


multiline_string = """This
is a
multiline
string."""

# lines = multiline_string.splitlines()
lines = multiline_string.split()

print("Original string:", multiline_string)


print("\nSplit the said multiline string into a list of lines:")
print(lines)
