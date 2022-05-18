# Test Environment

yolo = [1, True, 15.5, "Nay", 10, 20, 15, 40, 50]

def swapPositions(yolo, a, b):
     
    # popping both the elements from list
    first_ele = yolo.pop(a)  
    second_ele = yolo.pop(b-1)
    
    # inserting in each others positions
    yolo.insert(a, second_ele) 
    yolo.insert(b, first_ele) 
     
    return yolo
 
# Driver function

a = int(input("Please enter an index number:\t"))
b = int(input("Please enter another index number:\t"))
 
print(swapPositions(yolo, a-1, b-1))



