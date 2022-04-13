# Omercan
# April 12 2022
# Ex 23 Q6
# Finding the year in which the population will reach 100 000 000.

year = 1980
population = 24000000
rate = 0.055

while True:
    num = 100000000
    if num == num:
        population += rate * population
        year += 1

    if population >= num:
        print("Population will reach 100 million by the year {}".format(year))
        break