#Print the sum of the current number and the previous number





n=int(input("Enter the number="))

privious_num=0
for number in range(1,n+1):
    sum=privious_num+number
    print(f"Current number:{number}, Previous number:{privious_num},Sum:{sum}")
    privious_num=number


# n=3

# privious_num=0

# for number in range(1,n+1):
#     sum=privious_num+number
#     # print(f"Current number:{number}, Previous number:{privious_num},Sum:{sum}")
#     print("Current NUMBER:",number, "Previous NUMBER:",privious_num,"Sum=",sum)
#     privious_num=number
    

    