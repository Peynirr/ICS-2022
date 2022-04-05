# Omercan
# April 4 2022
# Practice While Loops - Q3
# Finding Numbers that are a Multiple of 5 and Divisible by 7 between 1500 and 2700
 
num1 = 1500
num2 = 2700

while num1 <= num2:
    num1 += 1
    n = num1
    if n %7 == 0 and n % 5 == 0:
        print(n)
