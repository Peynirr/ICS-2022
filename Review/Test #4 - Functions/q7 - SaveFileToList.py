# Omercan
# May 17 2022
# Review - Q7
# Saving a File to a List
 
fileRead = open("view.txt", 'r') #Variable designated to reading the file
 
#Process
while fileRead:
    line = fileRead.readline()
    if not line:
        break;
    view = line.strip()
    #Output
    print(view)

#Closes the file
fileRead.close()