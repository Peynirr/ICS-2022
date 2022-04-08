# Omercan
# April 7 2022
# Ex 22 Q3
# Displaying and Randomly Flipping a Coin; Heads or Tails

import random
import time

#Fixed Variables
heads = 0
tails = 0

#Input
flips = int(input("Please enter the number of times you want to flip the coin:\t"))

#Process
for i in range(flips):
    rand = random.choice(["Heads","Tails"])
    print(rand)
    time.sleep(0.75) #Time set to slow down the program

    if rand == "Heads":
        heads += 1 #Adds 1 point to everytime the flip lands on heads
    
    else:
        tails += 1 #Adds 1 point to everytime the flip lands on tails

percentHeads = heads/flips * 100 #Finds the percent, then multiples by 100 to get a whole number
percentTails = tails/flips * 100

#Output
print("The percent of heads was:\t{:.2f}%".format(percentHeads))
print("The percent of tails was:\t{:.2f}%".format(percentTails))
