# Omercan
# May 18 2022
# Review Q5e
# Swaps Two Elements in a Lit

#List
yolo = [1, True, 15.5, "Nay", 10, 20, 15, 40, 50]

#Input
a = int(input("Enter the first index:  "))
b = int(input("Enter the second index:  "))

#Function
def swap(yolo, a, b):
    #Creates a New List
    newYolo = yolo
    
    #Pops both elements
    firstElement= newYolo.pop(a)
    secondElement= newYolo.pop(b-1)

    #Inserts removed indexes in swapped positions
    newYolo.insert(b-1, firstElement)
    newYolo.insert(a, secondElement)
    
    return newYolo

print(swap(yolo, a, b))