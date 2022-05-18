# Omercan
# May 17 2022
# Review Q5a
# Returning the Smallest Value and the Index of a List

#List
foobar = ["toronto", "vancouver", "montreal", "calgary", "halifax" , "St. John’s"]

def findSmall(foobar):
    foobar.sort()
    print("The smallest value in is list is " + foobar[1])
findSmall(foobar)
