# Omercan
# May 9 2022
# Ex 30 Q5b
# Calling a Function In a Small Program 
import time

print("Before we start, we need to collect some data:\n")
time.sleep(0.69)
#Input
width = int(input("Please enter the width:  "))
time.sleep(0.69)
height = int(input("Please enter the height:  "))
time.sleep(0.69)
symbol = str(input("Please enter your symbol of choice:  "))
time.sleep(0.69)

print()
print("Thank you!\n")
time.sleep(1)

#Process
def printRectangle(symbol, width, height):
    #For loop
    for i in range(0, height + 1):
        #Output of custom art
        print(symbol * width) 

#Output
printRectangle(symbol, width, height) #Prints the rectangle for the first time
time.sleep(0.69)

print("Hello World!") #First message
time.sleep(0.69)

printRectangle(symbol, width, height) #Prints the rectangle for the seconds time
time.sleep(0.69)

print("ICS201") #Second message
time.sleep(0.69)

printRectangle(symbol, width, height) #Prints the rectangle for the third and final time