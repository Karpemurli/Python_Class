

#read the file


try:
    fp=open(r'D:\python\14-File handling\text.txt','r') 
    print(fp.read())
    fp.close()
except FileNotFoundError:
    print("check path..")