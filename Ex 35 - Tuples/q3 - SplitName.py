# Omercan
# May 16 2022
# Ex 35 Q3
# Spliting the First Name and Last Name in a String

#Function
def splitName(fullName):
    if type(fullName) != str:
        #Outputs if fullName is not a String
        return (None, None)
    
    else:
        #Finds a space starting from the beginning of the string
        fName = (fullName[:(fullName.find(" "))])
        #Finds a space starting from the end of the string
        lName = (fullName[(fullName.find(" ") +1):])

        if fullName.find(" ") == -1: #Outputs if there is no space 
            return (fullName + ", " + str(None))
    
        else:
            return (fName + ", " + lName)

#Call Function
print(splitName('Omercan Ozkan'))