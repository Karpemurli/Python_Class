# How can you use a loop to generate a multiplication table for a given number?



Nm=int(input("Enter the number="))


for i in range(1,11):
    print(f"{Nm}*{i}={Nm*i}")