
# #write kasa karayach

# # Q. how we can write the data into a file?


# fp=open(r"D:\python\14-File handling\text.txt","a")
# fp.write("javascript is easy..")
# fp.close()





with open(r"D:\python\14-File handling\text.txt","a") as fp:
    fp.write("\n murali is name....")



with open(r"D:\python\14-File handling\text.txt",'r') as ss:
    print(ss.read())
    
    
    

