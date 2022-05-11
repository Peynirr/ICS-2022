# Omercan
# May 10 2022
# Ex 31 Q6
# Printing a rectangular pattern using functions

#Input
width = int(input("Please enter the width:  "))
height = int(input("Please enter the height:  "))
symbol = str(input("Please enter the symbol of choice:  "))

#Process
def printRectangle(symbol, width, height):
    #For loop
    for i in range(0, height + 1): 
        #Output
        print(symbol * width)
printRectangle(symbol, width, height)