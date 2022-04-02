# Omercan
# Feb 23 2022
# ex 5 q3 
import math

print("Hello, let's find the total cost of the apples, oranges, pears, and plums!")

#input
costApples = float(input("Please enter the cost of the Apples:\t"))
costOranges = float(input("Please enter the cost of the Oranges:\t"))
costPears = float(input("Please enter the cost of the Pears:\t"))
costPlums = float(input("Please enter the cost of the Plums:\t"))

#process
totalCost = float(costApples + costOranges + costPears + costPlums) #cost of fruits added up

#output
print("The apples cost ${:.2f}, the oranges cost ${:.2f}, the pears cost ${:.2f}, and the plums cost ${:.2f}. The total cost is ${:.2f}".format(costApples, costOranges, costPears, costPlums, totalCost))