# Omercan
# April 8 2022
# Practice Q5
# Printing a Table Containing Values from 1 to 40 that spaces by 5 - might wanna change the code

#Process
print("--------------------------------------------------------\n--Value-------Squared----------Cubed-------Square Root--") #Table Header

for num in range (1, 101): #Range from 1-101
    squared = num * num #Squared Formula
    cubed = squared * num #Cubed Formula
    squareRoot = num ** 0.5 #Square Root Formula

    if num == 11:
        print("--------------------------------------------------------\n--------------------------------------------------------")

    elif num == 21:
        print("--------------------------------------------------------\n--------------------------------------------------------")

    elif num == 31:
        print("--------------------------------------------------------\n--------------------------------------------------------")

    elif num == 41:
        print("--------------------------------------------------------\n--------------------------------------------------------")

    elif num == 51:
        print("--------------------------------------------------------\n--------------------------------------------------------")
    
    elif num == 61:
        print("--------------------------------------------------------\n--------------------------------------------------------")
    
    elif num == 71:
        print("--------------------------------------------------------\n--------------------------------------------------------")
    
    elif num == 81:
        print("--------------------------------------------------------\n--------------------------------------------------------")

    elif num == 91:
        print("--------------------------------------------------------\n--------------------------------------------------------")

    elif num == 101:
        print("--------------------------------------------------------\n--------------------------------------------------------")

    print("{:5,d}{:15,d}{:16,d}{:17.7f}".format(num, squared, cubed, squareRoot))

print("--------------------------------------------------------\n--------------------------------------------------------") #Table Footer