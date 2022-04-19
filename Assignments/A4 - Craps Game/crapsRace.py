import random
import time

earnings = int(100)

#Input
name = input("Please enter your name:\t")
roll = int(input("Please enter the amount of times you want to roll:\t"))
bet = int(input("Please enter the amount of money you want to bet (MUST BE LESS THE AMOUNT YOU HAVE):\t"))
while bet <= 0 or bet > earnings:
    bet = int(input("Please enter a valid number that is no more than $100:\t"))

#Process
    for i in range(roll):
        dice1 = random.randrange(1, 7)
        time.sleep(0.5)
        dice2 = random.randrange(1, 7)
        time.sleep(0.5)
        print("{}, {}".format(dice1, dice2))

totDice = dice1 + dice2

if totDice == 2 or totDice == 3 or totDice == 12:
    print("You lose.")
    earnings -= bet
if totDice == 7 or totDice == 11:
    print("You win.")
    earnings += bet
else:
    print("Total score has been stored to your goal. Keep rolling until you get your goal or a 7.")



