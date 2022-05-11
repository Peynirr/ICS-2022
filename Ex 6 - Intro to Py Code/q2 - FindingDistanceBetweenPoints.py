# Omercan
# February 26 2022
# Ex 6 Q2
# Finding The Distance Between Points
import math

#[x, y] coordinates
point1 = [3, 4]
point2 = [6, 9]

#Process
distance = math.sqrt(((point1[0] - point2 [0]) ** 2) + ((point1[1] - point2[1]) ** 2))

#Output
print("The distance between the two points were {:.2f}.".format(distance))