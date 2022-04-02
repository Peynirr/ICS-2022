# author Omercan
# Date 24 Feb. 2022

# q 1 Perimeter and Area of Rectangle

#input
length = float(input("Please enter the length of the Rectangle:\t "))
width = float(input("Please enter the width of the Rectangle:\t "))

#process
perimeter = 2 * (length+width)
area = length*width

#output
print("The perimeter of a rectangle is ", perimeter, ", ", "and the area of the rectangle is ", area, ".")