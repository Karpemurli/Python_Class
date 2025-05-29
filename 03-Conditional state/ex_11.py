# Write a Python program to check if a triangle is equilateral, isosceles or scalene.
# Note :
# An equilateral triangle is a triangle in which all three sides are equal.
# A scalene triangle is a triangle that has three unequal sides.
# An isosceles triangle is a triangle with (at least) two equal sides.
# Expected Output:

# Input lengths of the triangle sides:                                    
# x: 6                                                                    
# y: 8
# z: 12                                                                   
# Scalene triangle


x=float(input("Input length of side x:"))
y=float(input("Input length of side y:"))
z=float(input("Input length of side z:"))

if(x + y > z) and (x + z > y) and (y + z > x) :
    if x == y ==z:
        print("Equilateral triangle")
    elif x == y or y == z or x == z:
        print("Isosceles triangle")
    else:
        print("Scalene triangle")
else:
    print("Not a valid triangle")
    
