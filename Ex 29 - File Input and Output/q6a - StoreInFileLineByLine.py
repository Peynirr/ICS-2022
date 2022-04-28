# Omercan
# April 27 2022
# Ex 29 - Q6a
# Creating a File and Adding Text to it

#List
hamlet = ["To", "be", "or", "not", "to", "be", "that", "is", "the", "question"]

#Process
fileWrite = open("sample.txt", 'w') #Creates the file
fileAppend = open("sample.txt", 'a') #Adds to the file

for element in hamlet: #Loop
    fileAppend.write(str(element) + "\n") #Writes then skips a line for every element in the list

fileWrite.close() #Closes the file