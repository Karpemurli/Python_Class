# Write a Python program to find the first appearance of the substrings 'not' and 'poor' in a given string. If 'not' follows 'poor', replace the whole 'not'...'poor' substring with 'good'. Return the resulting string.
# Sample String : 'The lyrics is not that poor!'
# 'The lyrics is poor!'
# Expected Result : 'The lyrics is good!'
# 'The lyrics is poor!'

sample_string ='the lyrics is not that poor'
sample_string0='The lyrics is poor!'

not_p=sample_string.find('not')
poor_p=sample_string.find('poor')

if not_p < poor_p and not_p !=-1 and not_p != -1:
    sample_string=sample_string[:not_p]+'good'+sample_string[poor_p+4:]
else:
    print('No match found')
    

print(sample_string)
print(sample_string0)

