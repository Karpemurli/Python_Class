# 5.  Write a Python program that takes a text file as input and returns the number of words of a given text file.
# Note: Some words can be separated by a comma with no space.


try:
    filepath=r'D:\python\14-File handling\text1.txt'
    with open(filepath,'r') as f:
        
        # co=f.read()
        
        # words=co.split()
        # # count=len(words)
        
        co=0
        for line in f:
            words=line.split()
            co+=len(words)
            
        
        print(f'The file {filepath} contains {co} words.')
except FileNotFoundError:
    print('The file does not exist.')
    
except Exception as e:
    print('An error occurred:',e)

