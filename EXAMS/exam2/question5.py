# Question 5: Word Frequency in a Sentence
# Write a Python program to count the frequency of words in a given sentence:
# 1.	Accept a sentence from the user.
# 2.	Split the sentence into words and count the occurrences of each word.
# 3.	Use a dictionary to store the word frequencies.
# 4.	Print the word and its frequency in the format: word: frequency.

sentence=input("Enter a sentence=")

words=sentence.split()

word_frequency={}

for i in words:
    if i in word_frequency:
        word_frequency[i] +=1
    else:
        word_frequency[i]=1

for i, frequency in word_frequency.items():
    print(f"{i}: {frequency}")