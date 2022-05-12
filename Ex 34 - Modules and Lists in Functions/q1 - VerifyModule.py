# Omercan
# May 12 2022
# Ex 34 Q1
# Verify module

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
isNumber() #Call function