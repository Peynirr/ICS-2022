# Omercan
# March 22 2022
# ex 15 q4 - finding the smallest value within 3 numbers and prints the smallest value 

#input
a = int(input("Please enter the first number:\t"))
b = int(input("Please enter the second number:\t"))
c = int(input("Please enter the third number:\t"))

smallest = 0

#process
if a < b and a < c:
        smallest = a

elif b < c:
    smallest = b

else:
    smallest = c

#output
print("{} is the smallest number of the three numbers.".format(smallest))