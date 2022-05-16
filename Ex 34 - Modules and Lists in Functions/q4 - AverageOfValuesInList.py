# Omercan
# May 12 2022
# Ex 34 Q4
# Checking the Average in a List
import q3_VerifyNumList

check = True

#Function
def listAvg(lst):
    total = 0
    for x in range(len(lst)):
        if q3_VerifyNumList.isNumList(lst, check):
            total += lst[x]
        else:
            print("Invalid. Cannot calculate the average using values that are not numbers!")
            break
        if x == len(lst) - 1:
            average = total / (len(lst))
            return ("The average of these numerical values is {}.".format(average))

#Output
print(listAvg([6, 9, 4, 2, 0])) #You may change the elements to test the outputs