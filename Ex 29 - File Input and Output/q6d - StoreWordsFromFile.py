# Omercan
# April 27 2022
# Ex 29 Q6d
# Storing each word in a list using a for loop

fileRead = open("sample.txt", 'r') #Variable designated to reading the file

#Process
for line in fileRead:
    #Output
    print(line.strip())

#Closes the file
fileRead.close()