# 2. Write a python program to find the longest words.



try:
    fp=r'D:\python\14-File handling\text.txt'
    with open(fp,'r') as f:
        text=f.read()
        longest_words=max(text.split(),key=len)
        print(f"The longest word in the file is: {longest_words}")
    
    
except FileNotFoundError:
    print("The file does not exist.")
except Exception as e:
    print(e)


