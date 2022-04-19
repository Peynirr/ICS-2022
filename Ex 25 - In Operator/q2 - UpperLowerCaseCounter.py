# Omercan
# April 19 2022
# Ex 25 Q2
# Counting the Number of Uppercase and Lowercase Letters in a Sentence Written by the User

#Input
sentence = input("Please enter a sentence you wish to input:\n\n")
countUpper = 0
countLower = 0

#Process
for charactersUpper in sentence:
    if charactersUpper in "ABCDEFGHIJKLMOPQRSTUVWXYZ":
        countUpper = countUpper + 1

for charactersLower in sentence:
    if charactersLower in "abcdefghijklmopqrstuvwxyz":
        countLower = countLower + 1

#Output
print("The count for upper characters is {}, and the count for lower characters is {}.".format(countUpper, countLower))
