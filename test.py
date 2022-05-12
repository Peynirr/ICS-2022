# Test


#List
def average(list): 
    result = sum(list) / len(list) 
    return result 

listSize = 3
list = [68, 68, 71, 71, 71, 75, 71, 78, 91, 98, 75, 71, 84]
print(average(list))



for i in range(0, listSize):
    element = input("Enter anything at index {}:\t".format(i))
    list.append(element)

def isNumber(element):
    try:
        value = int(element)
        print(True)
    except ValueError:
        try:
            value = float(element)
            print(True)
        except ValueError:
            print(False)
isNumber(element) #Call function