# Omercan
# May 11 2022
# Ex 32 Q5
# Finding the Distance between Two Sets of Coordinates in a Function
import math

def lineDistance():
    #Coordinates
    point1 = [3, 4]
    point2 = [6, 9]

    #Process
    distance = abs(math.sqrt(((point1[0] - point2 [0]) ** 2) + ((point1[1] - point2[1]) ** 2)))

    #Output
    print("The distance between the two points were {:.2f}.".format(distance))
lineDistance()