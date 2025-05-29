
#addition
import numpy as ss 

A=ss.array(
    [
        [1,2,3],
        [4,5,6],
        [7,8,9]
    ]
)


B=ss.array(
    [
        [9,8,7],
        [6,5,4],
        [3,2,1]
    ]
)

# result=A + B 
result=ss.add(A,B)
print("Add=\n", result)

