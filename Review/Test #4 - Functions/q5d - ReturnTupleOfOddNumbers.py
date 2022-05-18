# Omercan
# May 18 2022
# Review Q5d
# Returns a Tuple of all Odd numbers in the stuff list

#List
stuff = [-5, 34, 18, 9]

#Function
def getOdd(stuff):
    newStuff =[]
    for i in stuff:
        if i % 2 !=0:
            newStuff.append(i)
    print(tuple(newStuff))

#Call Function
getOdd(stuff)
