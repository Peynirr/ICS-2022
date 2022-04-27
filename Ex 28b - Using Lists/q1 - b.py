# Omercan
# April 26 2022
# Ex 28b Q1b
# Changing negative values to positive values in a list

#List
two = [1, 2, -3, 4, 6, 7, -8, -9, 10] #Used for verifying

#Process
for i in range(len(two)):
   posTwo = map(abs, two)
print(list(posTwo)) #Output