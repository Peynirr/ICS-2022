# Omercan
# May 12 2022
# Ex 34 Q3
# Checking if all Elements in a List are a Number

#List
list = []

#Number of elements in the list
listSize = int(input("Please enter the list size:\t"))

#For loop to add to the list
for i in range(0, listSize):
    element = input("Enter anything at index {}:\t".format(i))
    list.append(element)

def average(num):
    sum_num = 0
    for t in num:
        sum_num = sum_num + t           

    avg = sum_num / len(num)
    return avg
    
print("The average is", average([18, 25, 3, 41, 5]))

#Function
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