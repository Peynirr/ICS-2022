# Omercan
# April 26 2022
# Ex 28b Q1h
# Finding the median in a list with given values
from statistics import median

#List
two = [1, 2, 3, 4, 6, 7, 8, 9, 10]

#Process
twoLength = len(two)

if twoLength % 2:
    print("The median of the following list is", median(two),)