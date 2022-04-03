# Omercan
# April 1 2022
# Ex 19 Q2
# Determining if Password is Strong Enough

password = "ICS2O1"
attempts = 1

#input
userPassword = input("Please enter your password:\t")

#process
while attempts < 3 and userPassword != password :
    attempts += 1
    userPassword = input("Incorrect Password. Please try again:\n\n")

if userPassword != password:
    print("Incorrect password, you are locked out after 3 attempts. You may not try again.")

else: 
   print("Correct password. Welcome!")