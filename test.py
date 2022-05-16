# Test



#List
list = []
 
#Number of elements in the list
listSize = int(input("Please enter the list size:\t"))
 
#For loop to add to the list
for i in range(0, listSize):
    element = input("Enter anything at index {}:\t".format(i))
    list.append(element)

def num():
    print(list.isnumeric())

num()

def listToString(): 
    
    # initialize an empty string
    string = "" 
    
    # traverse in the string  
    for ele in list: 
        string += ele  
    
    # return string  
    return string 