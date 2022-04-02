# Omercan
# April 1 2022
# ex 19 q1
# Positive Integer Smallest Power of Two Loop

num = int(input("Please enter a positive integer:\n\n"))

#process
while num < 1:
    print("That is a positive integer!") #output
    break

n = 0
print('num , 2**n')

while num >= 2 ** n:
    print(num, 2 ** n) #output
    break
