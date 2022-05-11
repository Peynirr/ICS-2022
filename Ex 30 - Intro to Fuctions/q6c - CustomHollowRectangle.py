# Omercan
# May 10 2022
# Ex 30 Q6c
# Printing a Hollow Rectangle Through Custom User Input

#Input
rows = int(input("Please enter the number of rows: "))
length = int(input("Please enter the length: "))

#Process
def hollow():
    for i in range(rows):
        for k in range(length):
            if i == 0 or i == rows - 1 or k == 0 or k == length - 1:
                print('*', end = "")
            else:
                print(" ", end = "")
        print()
hollow()