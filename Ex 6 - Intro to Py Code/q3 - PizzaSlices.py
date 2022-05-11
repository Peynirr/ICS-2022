# Omercan
# February 26 2022
# Ex 6 Q3
# Calculating the Slices of Pizza for Each Person
import math

#Input
user = int(input("Please enter the number of people at the party:\t"))
slices = int(32)

#Process
eachSlices = slices // user
leftoverSlices = slices % user
normalDiv = slices / user

#Output
print("Option 1: {} slices each, {} left over".format(eachSlices, leftoverSlices))
print("Option 2: {:.2f} slies each".format(normalDiv))

