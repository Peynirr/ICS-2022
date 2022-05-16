# Omercan
# May 12 2022
# Ex 34 Q4
# Checking the Average in a List

list = [3, 4]

#Function
def verify():
    import VerifyModule

def isNumber(element):
    
    try:
        value = int(list)
        int(isinstance(list))
        listAvg(list)
    except ValueError:
        try:
            value = float(list)
            listAvg(list)
        except ValueError:
            print("Cannot calculate the average of non-numerical values.")
isNumber(list) #Call function

def average(list):
    return sum(list) / len(list)

def listAvg(list):
    if (all([isinstance(item, int) for item in list])):
        avg = average(list)
        print("Sum is {}.".format(sum))
    else:
        print("Cannot calculate the average of non-numerical values.")
listAvg(list)