divisor = 3

number = int(540)

test = number

count = 2

while(test % divisor == 0):
   test = test // divisor
   count = count + 1

print(str(number) + " has " + str(count) + " divisors")