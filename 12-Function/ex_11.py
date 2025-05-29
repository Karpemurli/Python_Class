#  Write a Python program to reverse a string.

def reverse(input_string):
    return input_string[::-1] 

string="Murali karape..."

reversed = reverse(string)

print("Original string:",string)
print("Reversed string:", reversed)