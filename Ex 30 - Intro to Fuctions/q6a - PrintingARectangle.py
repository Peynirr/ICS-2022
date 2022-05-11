# Omercan
# May 10 2022
# Ex 30 Q6a
# Printing a Shape Using Functions

#Input
width = int(21)
height = int(1)
symbol = str("*")

#Process
def solid(symbol, width, height):
    #For loop
    for i in range(height + 1): 
        #Output
        print(symbol * width)
solid(symbol, width, height)