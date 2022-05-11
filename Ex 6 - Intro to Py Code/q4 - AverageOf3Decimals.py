# Omercan
# February 26 2022
# Ex 6 Q4
# Finding the average of 3 decimal points
import math

#Input
decimal1 = float(input("Please enter decimal 1:\t"))
decimal2 = float(input("Please enter decimal 2:\t"))
decimal3 = float(input("Please enter decimal 3:\t"))

#Process
sum = decimal1 + decimal2 + decimal3
average = sum / 3

#Output
print("{:>10}".format(decimal1))
print("{:>10}".format(decimal2))
print("{:>10}".format(decimal3))
print("------------")
print("{:>10.2f}".format(average))

print("The average of the three decimals is {:.2f}".format(average))