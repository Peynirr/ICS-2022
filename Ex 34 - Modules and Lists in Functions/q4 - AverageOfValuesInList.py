# Omercan
# May 12 2022
# Ex 34 Q4
# Checking the Average in a List

list = []



#Function
def isNumber(element):
    for i in range(0, len(list)):
        element = input("Enter anything at index {}:\t".format(i))
        list.append(element)

    try:
        value = int(element)
        int(isinstance(list))
        listAvg(list)
    except ValueError:
        try:
            value = float(element)
            listAvg(list)
        except ValueError:
            print("Cannot calculate the average of non-numerical values.")
isNumber(element) #Call function

def average(list):
    return sum(list) / len(list)

def listAvg(list):
    if (all([isinstance(item, int) for item in list])):
        avg = average(list)
        print("Sum is {}.".format(sum))
    else:
        print("Cannot calculate the average of non-numerical values.")
listAvg(list)