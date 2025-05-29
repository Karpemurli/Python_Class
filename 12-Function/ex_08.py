
# Exercise 8: Define a function that accepts radius and returns the area of a circle

# import math

# radius=float(input("Enter the radius of the circle:"))

# # area=3.14*radius*radius
# area=math.pi*radius**2

# print("The area of the circle is:",area)

def calculate(radius):
    area=3.14*radius*radius
    return area

radius=float(input("Enter the radius of the circle:"))
area=calculate(radius)
print(f"The area of the circle with radius {radius} is: {area}.")