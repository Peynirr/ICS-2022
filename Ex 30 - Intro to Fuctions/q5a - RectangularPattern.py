# Omercan
# May 9 2022
# Ex 30 Q5a
# Printing a Rectangular Pattern Using Functions

#Input
width = int(input("Please enter the width:  "))
height = int(input("Please enter the height:  "))
symbol = str(input("Please enter your symbol of choice:  "))

#Process
def printRectangle(symbol, width, height):
    #For loop
    for i in range(0, height + 1): 
        #Output
        print(symbol * width)
printRectangle(symbol, width, height)