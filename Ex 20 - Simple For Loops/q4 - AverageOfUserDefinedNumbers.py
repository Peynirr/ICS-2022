# Omercan
# April 5 2022
# Ex 20 Q4
# Determining the Average of the Number of Integers Entered by User, Numbers Defined by User

#Input
numOfMarkEnt = int(input("Please enter the number of marks:\t"))
totalSum = 0

#Process
for n in range(numOfMarkEnt):
    marks = float(input("Please enter the mark:\t"))
    totalSum += marks

avg = totalSum / numOfMarkEnt #Calculating the Average

#Output
print("The average of the {} mark(s) is: {:.2f}%".format(numOfMarkEnt, avg))