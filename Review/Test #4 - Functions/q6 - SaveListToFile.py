# Omercan
# May 17 2022
# Review - Q6
# Saving a List into a Text File

#List
foobar = ["toronto", "vancouver", "montreal", "calgary", "halifax" , "St. John’s"]

#Process
fileWrite = open("view.txt", 'w') #Creates the file
fileAppend = open("view.txt", 'a') #Adds to the file

#For Loop
for element in foobar: 
    #Writes then skips a line for every element in the list
    fileWrite.write(str(element) + "\n")
    fileAppend.write(element + "\n")

#Closes the file
fileWrite.close()