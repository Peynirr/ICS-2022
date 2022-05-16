# Omercan
# May 12 2022
# Ex 34 Q3
# Checking if all Elements in a List are a Number
import q1_Verify

check = True

#Function
def isNumList(lst, check):
    for x in range(len(lst)):
        check = check and q1_Verify.isNumber(lst[x])
    if check == False: 
        return False
    else:
        return True

#List
l = [6, 9, 4, 2, 0] #You may change the elements to test the outputs

#Output
print(isNumList(l, check)) #Call function