 #Python Program to Print the Fibonacci sequence   
 
#  0 1 1 2 3 5 8 13 21
#  0+1=1
#    1+1=2
#      1+2=3
#        2+3=5
#          3+5=8
#            5+8=13
 #              8+13=21
 
 
 
 
# num=int(input('Enter the number='))
# n,m=0,1


# for i in range(0,num,1):
#     print(n)
#     t=n+m
#     n=m
#     m=t
    
num = int(input("Enter how many terms = "))
n1, n2 = 0,1 
i = 0

if num <=0:
    print("please enter positive number")
elif num == 1:
    print("The fabonacci series = ",n1)
    
else:
    while i < num:
        
        print(n1)
        n1,n2=n2,n1+n2
        i += 1
        