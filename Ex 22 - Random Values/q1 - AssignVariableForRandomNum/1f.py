# Omercan
# April 7 2022
# Ex 22 Q1f

import random

#Input
a = int(input("Enter value for a:\t"))
b = int(input("Enter value for b:\t"))
k = int(input("Enter value for k:\t"))

#Fixed Variable
abk = (a, a + b, a + b*2, a + k, a + k*2, a + k*b) #Variations

#Process
for f in range(8):
   print(random.choice(abk)) #Output
