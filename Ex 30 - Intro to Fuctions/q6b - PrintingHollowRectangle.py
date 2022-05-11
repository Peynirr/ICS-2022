# Omercan
# May 10 2022
# Ex 30 Q6b
# Printing a Hollow Rectangle

#Input
rows = int(8)
length = int(20)

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