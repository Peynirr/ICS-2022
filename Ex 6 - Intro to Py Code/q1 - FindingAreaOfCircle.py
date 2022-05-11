# Omercan
# February 25 2022
# Ex 6 Q1
# Finding the Area of a Circle
import math

print("Let's find the area of a circle!")

#Input
radius = float(input("Please enter the radius to find the area of a circle:\n"))

#Process
pi = math.pi
area = (2 * pi) * (radius ** 2)

#Output
print("The area of the circle is ", area)
