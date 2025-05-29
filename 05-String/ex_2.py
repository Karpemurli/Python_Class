# 2. Write a Python program to get a string made of the first 2 and last 2 characters of a given string. If the string length is less than 2, return the empty string instead.
# Sample String : 'w3school'
# Expected Result : 'w3ol'


str_d='w3school'

if len(str_d)<2:
    print("")
else:
    print(str_d[0:2]+str_d[-2:])  # last 2 characters
    

