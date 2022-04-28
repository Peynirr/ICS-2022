# Omercan
# April 27 2022
# Ex 29 Q6c
# Storing file contets in a list using readlines

fileRead = open("sample.txt", 'r') #Variable designated to reading the file

#Process
lines = fileRead.readlines()

#For loop
for wspace in range(len(lines)): #Removes whitespaces from each word
    lines[wspace] = lines[wspace].strip()

#Output
print(f"Lines = {lines}")

fileRead.close() #Closes the files