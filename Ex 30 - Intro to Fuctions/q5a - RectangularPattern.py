# Omercan
# May 5 2022
# Ex 30 Q5a
# Prints a rectangular pattern using defined functions

#Input
width = int(input("Please enter the width:  "))
height = int(input("Please enter the height:  "))
sym = str(input("Please enter your symbol of choice:  "))

#Process
def printRectangle(key):
    def Decoration(func):
        def wrapper(width, height):
            return func(width * key, height)
        return wrapper
    return Decoration

@printRectangle(sym)
def rectangle(width, height):
    return [width for i in range(height)]

#Output
print("\n".join(rectangle(width, height))) #Prints the custom rectangle