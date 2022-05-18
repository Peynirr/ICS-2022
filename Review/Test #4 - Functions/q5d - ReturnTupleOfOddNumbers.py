# Omercan
# May 18 2022
# Review Q5d
# Returns a Tuple of all Odd numbers in the stuff list

#List
stuff = [-5, 34, 18, 9]

#Function
def getOdd(stuff):
    newStuff = []
    for x in stuff:
        if x % 2 != 0:
            newStuff.append(x)
    print(tuple(newStuff))

#Call Function
getOdd(stuff)
