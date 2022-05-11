# Omercan
# February 25 2022
# Ex 0 Q4
# Unit Conversion Application

#Input
kilometers = float(input("Please enter your distance in kilometers (km):\t"))

#Process
miles = kilometers / 1.609
feet = kilometers * 3281
meters = kilometers * 1000

#Output
print("{} kilometers are {:.1f} units in miles, {:.0f} units in feet, and {:.0f} units in meters".format(kilometers, miles, feet, meters))