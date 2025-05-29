# 4. Write a Python program to copy the contents of a file to another file 



try:
    filepath1=r'D:\python\14-File handling\text.txt'
    filepath2=r'D:\python\14-File handling\text1.txt'
    
    
    with open(filepath1,'r') as s,open(filepath2,'w') as m:
        for line in s:
            m.write(line)
    print(f'File First {filepath1} copy to {filepath2}')

except FileNotFoundError:
    print('File not found')
except Exception as e:
    print('An error occurred:',e)
        
