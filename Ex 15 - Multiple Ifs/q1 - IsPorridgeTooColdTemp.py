# Omercan
# March 22 2022
# ex 14 q1 - determining if the temperature of the porridge is too hot or cold

#input
temperature = int(input("Please enter the temperature of the porridge:\t"))
MAX_TEMP = 50
MIN_TEMP = 5

#process
if temperature > MAX_TEMP:
   print("Porridge too hot")    #output

elif temperature < MIN_TEMP:
   print("Porridge too cold")   #output

else:
   print("Porridge just right - eat it all up.")    #output