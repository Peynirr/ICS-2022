# Omercan
# April 1 2022
# Ex 19 Q3
# Determining if a User Entered Integer is Number Less Than 1000

maxNum = 1000

#input
num = int(input("Please enter a positive integer less than 1000:\t"))

#process
while num < 1000 and num < 0:
    print("This is an invalid integer!")
    num = int(input("Please try again. Enter a positive integer less than 1000:"))

else:
    print("This is a positive integer!")