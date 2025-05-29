# Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If the given string already ends with 'ing', add 'ly' instead. If the string length of the given string is less than 3, leave it unchanged.
# Sample String : 'abc'
# Expected Result : 'abcing'
# Sample String : 'string'
# Expected Result : 'stringly'


str_a='abc'
str_b='string'

# if len(str_a)>=3:
#     str_a+='ing'
#     str_b+='ly'
    
# print(str_a)
# print(str_b)

if len(str_a)<3:
    print('')
else:
    str_a+='ing'
    str_b+='ly'
    print(str_a)
    print(str_b)    
