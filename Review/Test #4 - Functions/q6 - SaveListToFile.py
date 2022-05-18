# Omercan
# May 17 2022
# Review Q6
# Saving a List into a Text File
 
#List
foobar = ["Toronto", "Vancouver", "Montreal", "Calgary", "Halifax" , "St. John’s"]
 
#Process
fWrite = open("view.txt", 'w') #Creates the file
fAppend = open("view.txt", 'a') #Adds to the file
 
#For Loop
for ele in foobar:
    #Writes to the File
    fWrite.write(str(ele) + "\n")
    fAppend.write(ele + "\n")
 
#Closes the file
fWrite.close()