# Omercan
# March 2 2022

#input
fullName = input("Please enter your full name:\t")
vowels = 'aeiouAEIOU'

#process
vowelCounta = fullName.count('a')

vowelCounte = fullName.count('e')

vowelCounti = fullName.count('i')

vowelCounto = fullName.count('o')

vowelCountu = fullName.count('u')

vowelCountA = fullName.count('A')

vowelCountE = fullName.count('E')

vowelCountI = fullName.count('I')

vowelCountO = fullName.count('O')

vowelCountU = fullName.count('U')

vowelTotal = int(vowelCounta + vowelCounte + vowelCounti + vowelCounto + vowelCountu + vowelCountA + vowelCountE + vowelCountI + vowelCountO + vowelCountU)

#output
print("The amount of vowels in your name is {} vowels.".format(vowelTotal))
