import random
import time
y=0
z=0
x = int(input("Please enter how many times you would like to flip the coin\n"))
for i in range(x):
    r = random.choice(["Heads","Tails"])
    print(r)
    time.sleep(1)
    if r == "Heads":
        y +=1
    else:
        z +=1
print((y/x)*100  , " is the percent of heads")
print(z/x*100  , " is the percent of tails")