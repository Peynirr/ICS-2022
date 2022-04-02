# Omercan
# March 10 2022
# a3 q2
# HST Tax Calculator Between Adults and Elders

import math

#input
age = int(input("Please enter your age:\t"))
costOfMeal = float(input("How much was your meal?\t"))

#process
if age >= 65:
    totalCostSeniors = float(costOfMeal * 0.05 + costOfMeal)
    print("The total cost was ${:,.2f}".format(totalCostSeniors)) #output if age is 65+

else:
    totalCostNorm = float(costOfMeal * 0.13 + costOfMeal)
    print("The total cost was ${:,.2f}".format(totalCostNorm)) #output if age is less than 65
