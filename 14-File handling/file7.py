
try:
    fp=open(r"D:\python\14-File handling\text.txt",'r')
    print(fp.read())
    fp.close()
except FileNotFoundError:
    print("please check the path")
    
    
    #readline - convert in list.
try:
    fp=open(r'D:\python\14-File handling\text.txt','r')
    print(fp.readlines())
    fp.close()
except FileNotFoundError:
    print("The file does not exist.")
