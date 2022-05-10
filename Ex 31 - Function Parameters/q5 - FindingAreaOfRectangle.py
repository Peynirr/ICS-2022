# Omercan
# May 10 2022
# Ex 31 Q5
# Finding the area of a rectangle using a function

#Process
def putArea(length, width):
    #Input
    length = int(input("Enter the length:\t"))
    width = int(input("Enter the width:\t"))   
    area = length * width
    print("The area is: {} units".format(area))
putArea()