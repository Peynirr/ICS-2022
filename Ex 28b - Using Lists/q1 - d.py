# Omercan
# April 26 2022
# Ex 28b Q1d
# Swapping values from first and second index in a list

two = [1, 2, 3, 4, 6, 7, 8, 9, 10] #Used for verifying

#Process
index1 = two.index(1) #Collects from first index
index2 = two.index(2) #Collects from seconds index
two[index1], two[index2] = two[index2], two[index1] #Replaces

#Output
print(two)