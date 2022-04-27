# Omercan
# April 26 2022
# Ex 28b Q1e
# Finding the smallest value and its index location in a list

#List
one = [2, 3, 4, 6, 7, 1, 8, 9, 10] #Used for verifying

#Process
minValue = min(one)
indexLocation = one.index(minValue)

#Output
print("The minimum value in the list is {}, and the index location is {}.".format(minValue, indexLocation))