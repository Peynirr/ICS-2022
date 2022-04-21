# Omercan
# April 13 2022
# A4
# Playing Craps Game with 2 Dices with Betting
import random
from time import sleep
import sys

#Fixed Variables
#

print("Instruction:")
print("You have $100.")
print("Roll 2 dice. If the total is 2, 3, or 12, you lose. If the total is 7 or 11, you win.")
print("If you don't roll any of those numbers, you continue to roll under these conditions:")
print("Your first roll becomes the winning roll, and if you then roll a 7 before the winning roll, you lose.")

money = 500

def bet(money):
	print ("You currently have ${}".format(money))
	bet = input('Place your bet:\t')
	if bet.isdigit() is True:
		bet = int(bet)
		if bet > money or bet < 0:
			print ("Uh-oh, you don't have $%s to bet."%(bet))
			bet = int(input('Place your bet: $'))
	elif bet.isdigit() is False:
		print ("Please place your bet in only numbers.")
		bet = int(input('Place your bet: $'))
	return bet

def secondroll(previous):
	print ("*ROLL*")
	rollone = random.randint(1, 6)
	rolltwo = random.randint(1, 6)
	print(rollone, rolltwo)
	total = rollone + rolltwo
	sleep(0.75)
	if total == 7:
		return False
	elif total == previous:
		return True
	else:
		ans = secondroll(previous)
		return ans
	
def roll():
	print ("*ROLL*")
	rollone = random.randint(1, 6)
	rolltwo = random.randint(1, 6)
	print (rollone, rolltwo)
	sleep(.75)
	total = rollone + rolltwo
	if total in (2,3,12):
		return False
	elif total in (7,11):
		return True
	else:
		ans = secondroll(total)
		return ans

while money > 0:
	mybet = bet(money)
	money = money - mybet
	print ("You have ${} left to spend.".format(money))
	if roll():
		print ("You Win!")
		money = money + (2*mybet)
	else:
		print ("Crap Out!")
if money == 0:
    print ("you have no more money :(\nYou lose.")
    sys.exit("Exitting...")