# Omercan
# April 4 2022
# Practice While Loops - Q4
# Counting the Number of Even and Odd Numbers from a Series of Numbers

#Fixed Variables
numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9) #multiple numbers
countEven = 0
countOdd = 0

#Process
for x in numbers:
    if not x % 2:
        countEven += 1 #Counts by one each time it is divisible 2
    else:
        countOdd += 1 #Counts by one each time it is divisible 2

#Output
print("Number of even numbers:\t{}".format(countEven))
print("Number of odd numbers:\t{}".format(countOdd))

