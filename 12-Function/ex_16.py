# 1. Write a program that reads a string from keyboard and prints the unique words. Your program should convert input string to lower case.




def words():
    
    newline=input("Enter the Words=")
    
    words=newline.lower().split()
    
    unique_words=set(words)
    
    print("unique words:", unique_words)
    


words()


    