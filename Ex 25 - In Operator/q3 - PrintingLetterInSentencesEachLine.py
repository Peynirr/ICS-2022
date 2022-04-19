# Omercan
# April 19 2022
# Ex 25 Q3
# Printing Each Letter in a Sentence Entered by a User

#Input
sentence = input("Please enter a sentence you wish to input:\t")
letterCount = 0

#Process
print("\n")

for line in sentence:
    letterCount += 1 #Counts up by 1 for Each Letter
    print("Letter {} is {}".format(letterCount, line)) #Output