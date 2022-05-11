# Omercan
# February 24 2022
# Ex 0 Q1
# Finding the Perimeter and Area of Rectangle

#Input
length = float(input("Please enter the length of the Rectangle:\t "))
width = float(input("Please enter the width of the Rectangle:\t "))

#Process
perimeter = 2 * (length + width)
area = length * width

#Output
print("The perimeter of a rectangle is {} and the area of the rectangle is {}.".format(perimeter, area))