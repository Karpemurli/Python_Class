# Write a Python program to count the occurrences of each word in a given sentence.

word='Mango banana apple pear strawberry apple banana apple'

count={}

words=word.split()

for word in words:
    if word in count:
        count[word]+=1
    else:
        count[word]=1


print(count)


      

    

    