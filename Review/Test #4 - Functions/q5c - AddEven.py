# Omercan
# May 18 2022
# Review Q5c
# Finds Even Numbers in a List and Adds One to the Existing Value

#List
stuff = [-5, 34, 18, 9]

#Function
def addEven(stuff):
    num = 0
    for i in stuff:
        if i is not i%2:
            num += i
    print(num)

#Call Function
addEven(stuff)
