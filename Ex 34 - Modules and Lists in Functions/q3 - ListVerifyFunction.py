# Omercan
# May 12 2022
# Ex 34 Q3
# Checking if all Elements in a List are a Number
 
#List
list = []
 
#Number of elements in the list
listSize = 4
 
#For loop to add to the list
for i in range(0, listSize):
    element = [1, 2, 3, 4]
    list.append(element)
 
#Function
def isNumList(element):
    try:
        value = int(element)
        print(True)
    except ValueError:
        try:
            value = float(element)
            print(True)
        except ValueError:
            print(False)
isNumList(element) #Call function