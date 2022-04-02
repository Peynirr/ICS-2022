# Omercan
# March 24 2022
# a3 q4 
# Converting Seconds to Minutes, Days, or Hours

#input
sec = int(input("Please enter the number of seconds:\t"))
message = " "

#process
if sec >= 0 and sec < 60:
    seconds = format(sec % 60)
    message = "Seconds = " + seconds #outputs message with seconds

elif sec >= 59 and sec < 3599:
    minutes = format(sec // 60)
    seconds = format(sec % 60)
    message = minutes + " Minute(s), and " + seconds + " Second(s)." #outputs message with minutes and seconds

elif sec >= 3599 and sec < 86399:
    hours = format(sec // 3600)
    minutes = format((sec % 3600) // 60)
    seconds = format((sec % 3600) % 60)
    message = hours + " Hour(s), " + minutes + " Minute(s), and " + seconds + "Second(s)." #outputs message with hours, minutes, and seconds

elif sec >= 86400:
    days = sec // 86400
    hours = (sec % 86400) // 3600
    minutes = ((sec % 86400) % 3600) // 60
    seconds = ((sec % 86400) % 3600) % 60
    message = days + " Day(s), " + hours + " Hour(s), " + minutes + " Minute(s), and " + seconds + " Second(s)" #outputs message with days, hours, minutes, and seconds

else:
    print("Enter a number above 0. Please rerun and try again.") #if input is anything other than an integer

#output
print(message) #outputs the specific message from each of the if/elif statements