# Verify module

userInputList = []
userInput = input("Enter anything, seperating words in sentences:\t")

userInputList = userInput.split()
print(userInputList)

def isNumber(userInputList):
    try:
        #Convert to integer
        for i in userInputList:
            value = int(i)
            print(True)
    except ValueError:
        try:
            #Convert to float
            value = float(userInputList)
            print(True)
        except ValueError:
            print(False)
isNumber(userInputList) #Call function