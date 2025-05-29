# index method using update

mylist =input("enter a list:").split()

mylist=[item.strip() for item in mylist]

update=input("enter update word:")
new_word=input("enter new word:")

if update in mylist:
    index=mylist.index(update)
    mylist[index]=new_word
    print("update word:",mylist)
else:
    print("update word not found in list",update)

