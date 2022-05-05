# Omercan
# May 5 2022
# Ex 30 Q5a
# Prints a rectangular pattern using defined functions

def printRectangle():
    width = input("Please enter your width of choice:\t")
    height = input("Please enter your height of choice:\t")
    symbol = input("Please enter your choice of symbol for the rectange:\t")

    for sym in range(0, width):
        i = print(symbol , end = "")
    print(i * height)
printRectangle()