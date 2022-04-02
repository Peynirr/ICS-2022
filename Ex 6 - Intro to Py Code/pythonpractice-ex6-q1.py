import math

#name: Omercan
#date: 25 Feb. 2022
#course code: ISC2O1
#assignment: pythonpractice-ex6

print("Hello! Let's find the area of a circle!")

#input
radius = float(input("Please enter the radius to find the area of a circle:\n"))
pi = math.pi

#procedure
area = (2 * pi) * (radius ** 2)

#result
print("The area of the circle is ", area)

