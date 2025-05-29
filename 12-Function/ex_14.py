# Write a Python program that accepts a hyphen-separated sequence of words as input and prints the words in a hyphen-separated sequence after sorting them alphabetically.
# Sample Items : green-red-yellow-black-white
# Expected Result : black-green-red-white-yellow


def sort_hyphenated_sequence():
    # Accept input from the user
    input_sequence = input("Enter a hyphen-separated sequence of words: ")
    
    # Split the input string into a list of words
    words = input_sequence.split("-")
    
    # Sort the list alphabetically
    words.sort()
    
    # Join the sorted list back into a hyphen-separated string
    sorted_sequence = "-".join(words)
    
    # Print the sorted sequence
    print("Sorted sequence:", sorted_sequence)

# Call the function
sort_hyphenated_sequence()