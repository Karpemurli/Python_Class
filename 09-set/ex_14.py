# Write a Python program to find all the unique words and count the frequency of occurrence from a given list of strings. Use Python set data type.



# string=["a", "b", "c", "d", "e","b", "c", "d",]

# unique_words=set(string)

# word_count={word: string.count(word) for word in unique_words}

# print("unique words:",unique_words)
# print("word frequency:",word_count)



string=["a", "b", "c", "d", "e","b", "c", "d",]

unique_words=set(string)

for word in unique_words:
    print(f"{word}:{string.count(word)}")