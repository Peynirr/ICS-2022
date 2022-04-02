# Omercan
# March 22 2022
# ex 15 q6 - determining if the year entered by the user is a leap year

print("Let's find out if a year is a leap year.\n")

#input
year = int(input("Please enter a year:\t"))

#process
if year % 400 == 0:
    if year % 100 == 0:
        print("{} is a leap year".format(year)) #output

elif year % 4 == 0:
    if year % 100 != 0:
        print("{} is a leap year.".format(year)) #output

else:
    print("{} is not a leap year.".format(year)) #output