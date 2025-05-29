 #Python Program to Print the Fibonacci sequence   
 
#  0 1 1 2 3 5 8 13 21
#  0+1=1
#    1+1=2
#      1+2=3
#        2+3=5
#          3+5=8
#            5+8=13
 #              8+13=21
 


num=int(input('enter the positive number='))

n,m=0,1
count=0

while count < num:
    print(n)
    t=n+m
    n=m
    m=t
    count+=1
