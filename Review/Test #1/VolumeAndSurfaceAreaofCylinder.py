# Omercan
# March 3 2022

from cmath import cos
import math

#input
radius = float(input("Please enter the radius of the cylinder:\t")) #enter radius
height = float(input("Please enter the desired height: \t")) #enter height
print("Currently, the price per cm\u00b2 is $1.25.") #assigned price

#process
vCylinder = int(math.pi * radius ** 2 * height) 
saCylinder = int(2 * math.pi * radius * height + 2 * math.pi * radius ** 2)

#output
print("The volume of the cylinder is: {} cm\u00b3, and the surface area of the cylinder is: {} cm\u00b2".format(vCylinder, saCylinder))

print("Let's apply the cost to the surface area")

#process
totalCost = float(saCylinder * 1.25)

#final output
print("The cost to wrap the cylinder is ${}.".format(totalCost)) #total cost