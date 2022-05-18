# Omercan
# May 17 2022
# Review - Q7
# Saving a File to a List
 
fRead = open("view.txt", 'r') #Variable designated to reading the file
 
#Process
while fRead:
    line = fRead.readline()
    if not line:
        break;
    view = line.strip()
    #Output
    print(view)

#Closes the file
fRead.close()