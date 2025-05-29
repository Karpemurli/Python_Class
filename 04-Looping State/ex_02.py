#user inter a number and count the digits.


# num=10000

# i=0

# while num != 0:
#     num=num // 10
#     i=i+1
# print(i)
        




num=int(input("Enter a number:"))
count =0

while num != 0:
    num=num // 10
    count = count +1

print("Number of digits:",count)







# num=int(input("Enter a number:"))

# count=0
# while(num>0):
#     num=num//10
#     count=count+1
# print(count)