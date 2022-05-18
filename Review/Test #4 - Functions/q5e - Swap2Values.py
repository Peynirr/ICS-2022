# Omercan
# May 18 2022
# Review Q5e
# Swaps Two Elements in a List

#List
yolo = [1, True, 15.5, "Nay", 10, 20, 15, 40, 50]

#Function
def swapPositions(yolo, newYolo, a, b):
    
    newYolo = yolo
    #Pops both elements
    firstElement = newYolo.pop(a)  
    secondElement = newYolo.pop(b-1)
    
    #Inserts each position
    newYolo.insert(a, secondElement) 
    newYolo.insert(b, firstElement) 
    

#Input
a = int(input("Please enter an index number:\t"))
b = int(input("Please enter another index number:\t"))

#Call Function 
print(swapPositions(newYolo, a-1, b-1))