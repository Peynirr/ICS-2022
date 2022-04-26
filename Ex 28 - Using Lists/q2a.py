# Omercan
# April 25 2022
# Ex 28a Q2a

sample = [1, 3, 5, 3, 4, 3, 4, 7, 8]

for num in sample:
    if num > 0:
        sample.append(0)
    else:
        sample.append(num)

    print(sample)