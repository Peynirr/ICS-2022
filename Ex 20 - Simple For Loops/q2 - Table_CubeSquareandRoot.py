# Omercan
# April 5 2022
# Ex 20 Q2
# Printing a Table Containing Cube, Square, and Root Values from 1 to 40

#Process
print("--Value-------Squared----------Cubed-------Square Root--") #Table Header
    
for num in range(1, 41): #Range from 1-40
    squared = num * num #Squared Formula
    cubed = squared * num #Cubed Formula
    squareRoot = num ** 0.5 #Square Root Formula
    
    print("{:5,d}{:15,d}{:16,d}{:17.7f}".format(num, squared, cubed, squareRoot))

print("--------------------------------------------------------") #Table Footer