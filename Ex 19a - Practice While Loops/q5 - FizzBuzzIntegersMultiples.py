# Omercan
# April 5 2022
# Practice While Loops - Q5
# Iterating the integers that are multiples of five or three; or both using 'FizzBuzz'

#Fixed Variables
num = 0

#Process
while num <= 50:
    if num % 3 == 0 and num % 5 == 0: #If number is a multiple of both 3 and 5
        print("FizzBuzz, {}.".format(num))

    elif num % 3 == 0: #If number is only a multiple of 3
        print("Fizz, {}".format(num))

    elif num % 5 == 0: #If number is only a multiple of 5
        print("Buzz, {}".format(num))
        
    print(num) #Output
    num += 1
    