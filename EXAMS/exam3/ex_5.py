# 5. Create a function that counts the occurrences of each word in a given string. Example: word_count("hello world hello") → {'hello': 2, 'world': 1}


def word_count(input_string):
    words=input_string.split( )
    
    word_fre={}
    
    for word in words:
        word=word.lower()
        word_fre[word]=word_fre.get(word,0)+1
        
    return word_fre

input_string=input("Enter a word:")
result=word_count(input_string)

print("Word count:",result)