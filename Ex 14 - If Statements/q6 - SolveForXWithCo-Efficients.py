# Omercan
# March 21 2022
# ex 14 q6 - gathering values and solving for x
import sys

#input for b
a = input("Please enter the first integer:\t")

#process for a
if a.isdigit or "." in a:
    a = float(a)

else:
    print("Error. Please enter a valid integer again.")
    sys.exit()

#input for b
b = input("Please enter the second integer:\t")

#process for b
if b.isdigit or "." in b:
    b = float(a)

else:
    print("Error. Please enter a valid integer again.")
    sys.exit()

#final process
if a != 0:
    xIntercept = (b * -1)/a
    print("The x-intercwept is {:8.2f}.".format(xIntercept))

else: 
    print("The x-intercept cannot be found, the first value may be 0.")