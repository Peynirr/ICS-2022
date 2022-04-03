# Omercan
# April 3 2022
# Ex 19 Q4
# Asking the User to Guess the Value of a Letter from A to Z

letter = "O"

#input
guess = str(input("Please enter a CAPITAL single letter of your choice from A to Z:\t"))

#process
while guess <= str(9):
    guess = str(input("Invalid. Please enter a single letter:\t"))

else:
    while guess != letter:
        if guess > letter:
            print("You are wrong; go closer to A.")
            guess = str(input("Try again. Choose a single letter of your choice from A to Z:\t"))

        elif guess < letter:
            print("You are wrong; go close to Z.")
            guess = str(input("Try again. Choose a single letter of your choice from A to Z:\t"))
            
    else:
        print("You are correct. Congratulations!")