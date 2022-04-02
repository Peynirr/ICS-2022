# Omercan
# March 2 2022


#input
sentence = input("Please enter a sentence longer than 10 characters:\t")

print("Now we will chose 3 random numbers, please choose 3 numbers that does not exceed the limit of characters in your sentence and are single digit!")

num1 = input("Please enter the first number:\t")
num2 = input("Please enter the second number:\t")
num3 = input("Please enter the third and final number:\t")

#process

sentenceFinal = sentence[num1:num1] + sentence[num2:num2] + sentence[num3:num3]

numTot = num1 + num2 + num3

print("{}\n {}".format(sentenceFinal, numTot))

