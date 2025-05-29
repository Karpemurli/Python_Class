
# 7)	Write a program that uses a loop to repeatedly ask the user to enter integers. The loop will come to an end when zero is entered. After collecting all the integers, the program will compute and display the average of all the entered numbers.


total=0
count=0


print("enter intergers(Enter 0 to stop):")


while True:
    num=int(input("Enter a number:"))
    if num==0:
        break
    total+=num
    count+=1
    avg=total/count

print(f"Average:{avg}")

