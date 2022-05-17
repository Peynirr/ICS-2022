# Omercan
# May 16 2022
# Ex 35 Q3
# Spliting the First Name and Last Name in a String

#String
fullName = ('HarryPotter')

#Function
def splitName(fullName):
    if type(fullName) == str:
        if " " in fullName == True:
            names = fullName.split()
            tupNames = tuple(names)
            print(tupNames)

        else:
            if " " in fullName == False:
                newFullName = fullName + None
                names = newFullName.split()
                tupNames = tuple(names)
                print(tupNames)

    else:
        
        
        print("Error. This is not a string.")
        exit

splitName(fullName) #Call function