# Omercan
# April 26 2022
# Ex 26b Q1j
# Shifting values in a list to the right by one

#List
one = [1, 2, 3, 4, 6, 7, 8, 9, 10]

#Process
one = one[-1:] + one[:-1]

#Output
print("The list consists: " + str(one))