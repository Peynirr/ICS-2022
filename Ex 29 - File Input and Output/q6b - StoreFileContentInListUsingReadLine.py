# Omercan
# April 27 2022
# Ex 29 - Q6b
# Store each element from an existing file into a list

fileRead = open("sample.txt", 'r') #Variable designated to reading the file

#Process
while fileRead:
    line = fileRead.readline()
    
    if not line:
        break;

    newHamlet = line.strip()
    #Output
    print(newHamlet)

fileRead.close() #Closes the file