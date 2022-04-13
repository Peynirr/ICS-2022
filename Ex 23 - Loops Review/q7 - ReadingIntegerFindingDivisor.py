# Omercan
# April 12 2022
# Ex 23 Q7
# Processing an integer and finding and listing all of its divisors

#Input
number = int(input("Please input an integer:\t"))
print()

#Process
print("The divisors for the integer {} are:\n".format(number)) 

for i in range(1, number + 1):
    if number % i == 0:
        print(i)