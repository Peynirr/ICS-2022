# Omercan
# March 30 2022
# Ex 17 q7 - Redirecting User to Input a Positive Integer if User Enters a Negative Integer

#input
num = int(input("Please enter a positive number:\t"))

#process
while num <= 0:
    print("Try again")
    num = int(input("Please enter a positive number:\t"))
    break
    
else:
    print("Positive number")