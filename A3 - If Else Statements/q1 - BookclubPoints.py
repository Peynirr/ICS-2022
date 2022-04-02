# Omercan
# March 10 2022
# a3 q1
# Calculating the Total Points Based on the Number of Books Bought in a Month

#input
numberOfBooks = int(input("Please enter the number of books that you bought this month:\t"))

#process
if numberOfBooks < 0:
    print("Error. Please enter a positive number and try again.") #when a negative integer is entered
else:
    message = "You are awarded " #base message
    if numberOfBooks == 1: #0 points for 1 book
        message += "0 "
    elif numberOfBooks >= 2 and numberOfBooks <= 4: #5 points for 2-4 books
        message += str(5 * numberOfBooks)
    elif numberOfBooks >= 5 and numberOfBooks <= 8: #7.5 points for 5-8 books
        message += str(7.5 * numberOfBooks)
    elif numberOfBooks >= 9 and numberOfBooks <= 12: #10 points for 9-12 books
        message += str(10 * numberOfBooks)
    elif numberOfBooks >= 12: #15 points for 12+ books
        message += str(15 * numberOfBooks)

    message += " points!" #adds onto the process above

#output
print(message)
