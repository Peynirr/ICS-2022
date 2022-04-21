import random

def rollDice():
    die1 = random.randint(1,6)
    die2 = random.randint(1,6)
    x = int(die1 + die2)
    print('Roll', x)
    return x

def prog_info():
    print("You have three rolls of the dice to match a number you select.")
    print("Good Luck!!")
    print("---------------------------------------------------------------")
    print(f'You will win 2 times your wager if you guess on the 1st roll.')
    print(f'You will win 1 1/2 times your wager if you guess on the 2nd roll.')
    print(f'You can win your wager if you guess on the 3rd roll.')
    print("---------------------------------------------------------------")

def total_bank(bank):
    bet = 0 
    while bet <= 0 or bet > min([500, bank]):
        print(f"You have ${bank} in your bank.")
        a = input("Enter your bet (or Q to quit): ")
        if a == 'q': exit()
        bet = int(a)
    return bank, bet

def get_guess():
    guess = 0
    while (guess < 2 or guess > 12):
        try:
            guess = int(input("Choose a number between 2 and 12: "))
        except ValueError:
            guess = 0
        return guess

prog_info()
bank = 500

while True:
    bank,bet = total_bank(bank)
    guess = get_guess()

    if guess == rollDice():
        bank += bet
    elif guess == rollDice():
        bank += bet * .5
    elif guess == rollDice():
        bank = bank
    else:
        bank = bank - bet

    print(f'You have ${bank} in your bank.')
    print(f'Thanks for playing!\n')