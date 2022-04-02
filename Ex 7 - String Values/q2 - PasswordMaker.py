print("Lets create a password!")

#inputs

fName = input("Please enter your first name:\n")
lName = input("Please enter you last name:\n")
idNum = input("Enter your ID number:\n")

#process

pswFinal = fName[:2] + lName[-2:] + idNum[-4:]

#output

print("Thank you! Your password is:", pswFinal,) 
