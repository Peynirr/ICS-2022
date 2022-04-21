import random
def main():
    startingMoney = int(100)
    print()
    player_bet = int(input("Enter how much money you would like to bet:\t"))
    
    dice1 = (random.randint(1,6))
    dice2 = (random.randint(1,6))
    
    print("Dice roll 1: ", dice1)
    print("Dice roll 2: ", dice2)
    roll = dice1 + dice2
    print("Your roll: ", roll)
    rounds = input("Play again? (Y/N): ")
    while rounds != "n" and rounds == "y":
        if rounds == "n":
            print("Congratulations, you left with")
        if roll == 7 or roll == 11:
            print("You win $", player_bet, sep="")
            new_money = startingMoney + player_bet
            print("You have $", new_money, " remaining.", sep="")
        elif roll == 2 or roll == 3 or roll == 12:
            new_money = startingMoney - player_bet
            print("You lost $", player_bet, sep="")
            print("You have $", new_money, " remaining.", sep="")
        else:
            print("You push.")
            new_money = startingMoney
            print("You have $", new_money, " remaining.", sep="")
        break
main()