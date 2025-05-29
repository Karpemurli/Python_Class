# 5)	Given two strings, s1 and s2. Write a program to create a new string s3 made of the first char of s1, then the last char of s2, Next, the second char of s1 and second last char of s2, and so on. Any leftover chars go at the end of the result.


s1=input("Enter the First string(s1):")
s2=input("Enter the First string(s2):")
s3=""

s2_reversed=s2[::-1]

lenght=max(len(s1),len(s2))

for i in range(lenght):
    if i < len(s1):
        s3+=s1[i]
    if i < len(s2_reversed):
        s3+=s2_reversed[i]
    
print(f"\nresult: {s3}")
    
