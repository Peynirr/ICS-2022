# Omercan
# April 8 2022
# Ex 23 - Practice Q5
# Printing a Table that has the squared and cubed number for values from 1 to 100.
 
#Process
print("--------------------------------------\n--Value-------Squared----------Cubed--") 
 
for num in range (1, 101): #Range from 1-101
   squared = num * num #Squared Formula
   cubed = squared * num #Cubed Formula
 
   if num == 11:
       print("--------------------------------------")
 
   elif num == 21:
       print("--------------------------------------")
 
   elif num == 31:
       print("--------------------------------------")
 
   elif num == 41:
       print("--------------------------------------")
 
   elif num == 51:
       print("--------------------------------------")
 
   elif num == 61:
       print("--------------------------------------")
 
   elif num == 71:
       print("--------------------------------------")
 
   elif num == 81:
       print("--------------------------------------")
 
   elif num == 91:
       print("--------------------------------------")
 
   elif num == 101:
       print("--------------------------------------")
 
   print("{:5,d}{:15,d}{:16,d}".format(num, squared, cubed))
 
print("--------------------------------------\n--------------------------------------")