#Non-keyword based arguments

#function to add 3 numbers


# def adder(x,y,z):
#     print("Sum=",x+y+z)


##i am calling the functon

# adder(10,12,13)

##when we run above functon it will print sum as 35.


##let's see what happens when we pass more 3 argument 
##in the adder function


# adder(2,3,5,7,9)#TypeError: adder() takes 3 positional arguments but 5 were given


##so we solve they above problem as below.

def add(*num):
    sum=0
    for i in num:
        sum=sum+i
    print("Sum=",sum)
    
add(2,34,5)
add(2,3,5)








