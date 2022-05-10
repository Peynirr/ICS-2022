# Omercan
# April 29 2022
# Review - Q6
# Store each element from an existing file into a list
 
fileRead = open("review.txt", 'r') #Variable designated to reading the file
 
#Process
while fileRead:
    line = fileRead.readline()
    if not line:
        break;
    review = line.strip()
    #Output
    print(review)
fileRead.close() #Closes the file