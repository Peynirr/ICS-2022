# Omercan
# April 26 2022
# Ex 28b Q1i
# Creating a new list that has the same values shifted by one to the right

#List
one = [1, 2, 3, 4, 6, 7, 8, 9, 10]

#Process
three = one[-1:] + one[:-1]

#Output
print("The list labelled 'one' consists: " + str(one))
print("The new list labelled 'three' has values: " + str(three))