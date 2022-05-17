# Omercan
# May 17 2022
# Review Q5a
# Returning the Smallest Value and the Index of a List

#List
foobar = ["toronto", "vancouver", "montreal", "calgary", "halifax" , "St. John’s"]

def findSmall(foobar):
    minValue = min(foobar, key=len)
    tupNames = minValue.split()
    tupNames = tuple(minValue)
    print(tupNames)
findSmall(foobar)
