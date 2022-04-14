# Omercan
# April 13 2022
# A4
# Playing Craps Game with 2 Dices with Betting

#Fixed Variables
import sys
import random
import time


startingEarning = int(100)

#Input
name = input("Please enter your name:\t")
bet = int(input("How much would you like to bet? It must be a WHOLE number that is UNDER or EQUAL to $100:\t"))

#Checking the Validity of the Bet Placed
while bet > startingEarning:
    print("Try again") #If the betting price is over $100
    bet = int(input("Please enter a valid betting cost:\t"))
if bet < 0:
    print("Game exitting due to errors...") 
    quit() #Exits code
else:
    print("Thank you. We may continue.") # Output if the betting price is under or equal to $100

#Process of the Game
for dice in range(1):
    print("We are going to role 2 dices. Let's begin!")

    diceRoll1 = random.choice(['1', '2', '3', '4', '5', '6'])

    time.sleep(0.75) #Time set to slow down the program

    diceRoll2 = random.choice(['1', '2', '3', '4', '5', '6'])
    print("{}, {}".format(diceRoll1, diceRoll2))

    totDiceRoll = diceRoll1 + diceRoll2

    if totDiceRoll == "2" or "3" or "12":
        startingEarning -= bet
        print("You lose.")
        if bet <= 0:
            print("You are out of money, game over.")
            quit("Quitting...")
    else:
        if totDiceRoll == "7" or "11":
            startingEarning += bet #Adds the betted value to the earnings
            print("You win!")

