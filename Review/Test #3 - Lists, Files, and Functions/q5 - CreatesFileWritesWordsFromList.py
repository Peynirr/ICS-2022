# Omercan
# April 28 2022
# Review - Q5
# Creating a File and Adding Text from a List to it

#List
foobar = ["toronto", "vancouver", "montreal", "calgary", "halifax"]

#Process
fileWrite = open("review.txt", 'w') #Creates the file
fileAppend = open("review.txt", 'a') #Adds to the file

for element in foobar: #For Loop
    fileWrite.write(str(element) + "\n") #Writes then skips a line for every element in the list
    fileAppend.write(element + "\n")

fileWrite.close() #Closes the file