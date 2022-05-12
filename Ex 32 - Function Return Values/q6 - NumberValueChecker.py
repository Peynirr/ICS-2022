# Omercan
# May 11 2022
# Ex 32 Q6
# Checking an Argument if it's a Number Value

#Input
userInput = input("Please enter anything you want:\t")

#Process
def isNumber(userInput):
    try:
        #Convert to integer
        value = int(userInput)
        print(True)
    except ValueError:
        try:
            #Convert to float
            value = float(userInput)
            print(True)
        except ValueError:
            print(False)
isNumber(userInput) #Call function