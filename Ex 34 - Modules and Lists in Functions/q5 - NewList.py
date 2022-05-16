# Omercan
# May 12 2022
# Ex 34 Q5
# Copying an Existing List and Adding it to a New List

#List
list = [6, 9, 4, 2, 0] #You may change the elements to test the outputs

#Function
def copyList(list):
    newList = list.copy()
    newList.append(6.9) #You may add an integer/float or a string
    
    #Output
    print("The existing list was: {}".format(list))
    print("The new list is: {}.".format(newList))
copyList(list) #Call function