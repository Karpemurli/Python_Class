

def fact(n):
    if n == 1:
        return 1
    return n * fact(n-1)

print(fact(5))

# fact(5) ------> 5 * fact(5-1) = 5*4 =20
# fact(4) ------> 4 * fact(4-1) = 4*3 =12
# fact(3) ------> 3 * fact(3-1) = 3*2 =6 
# fact(2) ------> 2 * fact(2-1) = 2*1 =2 
# fact(1) ------> 1 * fact(1-1) = 1*1=1 
