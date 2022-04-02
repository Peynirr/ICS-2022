# Omercan
# March 24 2022
# q7 - finding the number of words in each sentence and the total number of characters

#input
sentence1 = input("Please enter your desired first sentence\n\n")
sentence2 = input("Please enter the second sentence:\n\n")

#process
splt1 = sentence1.split()   #splitting the sentences into words
splt2 = sentence2.split()

wordCount1 = len(splt1) #counting the individual words
wordCount2 = len(splt2)

replaceSent1 = sentence1.replace(" ", "")
replaceSent2 = sentence2.replace(" ", "")

totNumChar1 = len(replaceSent1) #count of the characters
totNumChar2 = len(replaceSent2)

AvgNumOfChar1 = round(totNumChar1 / totNumChar1, 1) #average number of characters for sentence 1
AvgNumOfChar2 = round(totNumChar2 / totNumChar2, 1) #average number of characters for sentence 2

if AvgNumOfChar1 > AvgNumOfChar2:
    print("\nSentence 1 is fancy.")
    if AvgNumOfChar1 < AvgNumOfChar2:
        print("\nSentence 2 is fancy.")
else:
    print("\nThese sentences are wordy.")
    