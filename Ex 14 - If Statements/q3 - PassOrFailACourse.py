# Omercan
# March 21 2022
# ex 14 - q3

print("Did you pass or fail a course? Let's find out.")

#input
courseMk = int(input("Please enter your course mark:\t"))

#process
if courseMk >= 50:
    print("You have passed the course, with an astounding {}%!".format(courseMk))
else:
    print("You have failed the course, with a {}%".format(courseMk))