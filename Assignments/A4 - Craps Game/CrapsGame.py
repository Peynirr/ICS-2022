# Omercan
# April 13 2022
# A4
# Playing Craps Game with 2 Dices with Betting
import random
import time
import sys

# Variable Dictionary
# dice1 - the first dice
# dice2 - the second dice
# gameFinal - determines if the players turn ends based on the results from the die
# goal - if the dice determines a number that is neither a winner or loser on the first roll
# bet - the bet placed
# firstBet - the first bet placed
# balance - the remaining/current balance that the player has (as the game goes on)
# totalDice - the sum of dice1 and dice2

def diceRoll():
    input("Press ENTER to roll!\n") #Prompts user to press enter to roll the dice
    
    dice1 = random.randrange(1, 7) #Rolls two dice from 1-6
    dice2 = random.randrange(1, 7)

    #Outputs the dice roll outcome
    print(f"Dice 1: {dice1}\nDice 2: {dice2}\n----------------------------\nSUM: {dice1} + {dice2} = {sum((dice1,dice2))}")
    return dice1, dice2 

def placedBet():
    #Validation of Bet
    while True:
        try:
            firstBet = int(input("Enter your bet:\t$"))  #User inputs the first bet
        except:
            continue

        if balance >= firstBet >= 1: 
            return firstBet
        elif firstBet < 0:
            sys.exit("Game exiting....")
        else:
            print("Invalid Bet. Please enter a bet that is valid!") #Warning that the bet is lower/higher than the balance

#Determines if the game ends or loops
balance = 100
while balance > 0: #Loops until the balance is less than 0
    print(f"Balance:\t${balance}")
    bet = placedBet()

    totalDice = sum(diceRoll()) #First roll total
    
    if totalDice in (7, 11): #If the sum of the dice is 7 or 11, user is a winner
        gameFinal = True

    elif totalDice in (2, 3, 12): #If the sum of the dice is 2, 3, or 12, user is a loser
        gameFinal = False

    else: #If the sum of the dice is another number than 7, 11, 2, 3, or 12, it is a goal
        gameFinal = None 
        goal = totalDice
        print("You have a goal to get in order to win. The goal is", goal)

#Loops until sum of dice equals the goal
    while gameFinal is None:
        totalDice = sum(diceRoll())

        if totalDice == goal:
            gameFinal = True

        elif totalDice == 7:
            gameFinal = False

        if gameFinal:
            print(f"You won ${bet}! Congratulations!")
            balance += bet  #Bet is added to balance if player wins
        else:
            print(f"You Lost ${bet}")
            balance -= bet  #Bet is subtracted from balance if player wins

print("Oh no! You ran out of money! GAME OVER") #Outputs if the player has no money left