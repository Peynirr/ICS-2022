# Omercan
# March 22 2022
# ex 15 q5 - determining if a student has earned a scholarship award

#fixed variables
bigVolunHours = 150
bigAverage = 90
bigEarning = 1000

goodVolunHours = 50
goodAverage = 80
goodEarning = 200

earning = 0

print("Let's determine if you have earned a scholarship award.\n")

#input
volunHours = int(input("Please enter the amount of volunteer hours:\t"))
average = int(input("Please enter your average mark:\t"))

#process
if volunHours >= bigVolunHours:
    if average >= bigAverage:
        earning = bigEarning

elif volunHours >= goodVolunHours:
    if average >= goodAverage:
        earning = goodEarning
    
else:
    earning = earning

#output
print("You have earned ${} from your volunteer hours and average mark.".format(earning))