# Omercan
# March 2 2022

#input
name1: str = input("Please input your full name:\t")

#output
print("Your name is this without the vowels in your name:")
for x in name1:
    if x in 'AEIOUaeiou':
        print('@', end='')
    else:
        print(x, end='')
