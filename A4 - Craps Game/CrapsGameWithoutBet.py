import random
import time

startingEarning = 100

#Input
roll = int(input("Please enter the number of times you want to roll the dice:\t"))

#Process
for i in range(roll):
    dice1 = random.randrange(1, 7)
    time.sleep(0.75) #Time set to slow down the program
    dice2 = random.randrange(1, 7)
    time.sleep(0.75) #Time set to slow down the program
    sumOfDice = dice1 + dice2
    print(dice1, ", ", dice2)

print("The two dice rolled were {}, and {}. The total sum of the two dices are {}".format(dice1, dice2, sumOfDice))

if sumOfDice == "2":
        print("You LOSE.")
    if sumOfDice == "3":
        print("You LOSE.")
    if sumOfDice == "12":
        print("You LOSE.")

    if sumOfDice == "7":
        print("You WIN.")
    if sumOfDice == "11":
        print("You WIN.")

    if sumOfDice == "1":
        print("Please continue. The sum {} will be stored for the future until you get a sum of 7.".format(sumOfDice))
    if sumOfDice == "4":
        print("Please continue. The sum {} will be stored for the future until you get a sum of 7.".format(sumOfDice))
    if sumOfDice == "5":
        print("Please continue. The sum {} will be stored for the future until you get a sum of 7.".format(sumOfDice))
    if sumOfDice == "6":    
        print("Please continue. The sum {} will be stored for the future until you get a sum of 7.".format(sumOfDice))
    if sumOfDice == "8":
        print("Please continue. The sum {} will be stored for the future until you get a sum of 7.".format(sumOfDice))
    if sumOfDice == "9":
        print("Please continue. The sum {} will be stored for the future until you get a sum of 7.".format(sumOfDice))
    if sumOfDice == "10":
        print("Please continue. The sum {} will be stored for the future until you get a sum of 7.".format(sumOfDice))

