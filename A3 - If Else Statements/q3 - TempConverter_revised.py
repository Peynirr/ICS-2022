# Omercan
# March 24 2022
# a3 q3
# Converting the Temperature Between Celsius and Fahrenheit Based on the Users Input

#input
print("Welcome to the temperature unit program!\n")
var = input("Please enter your unit of choice (f or c):\t") #original unit
num = int(input("Please enter a number of choice:\t"))

if var == "celsius" or "Celsius" or "CELSIUS" or "c" or "C":
    convertFah = (num * 9/5) + 32
    print("{} degrees celsius = {} degrees fahrenheit.".format(num, convertFah))
    if convertFah <= 40:
        print("Get inside and warm up! You will get hypothermia!")
    elif convertFah <= -40 and convertFah <= 10:
        print("It is cold, wear a warm jacket.")
    elif convertFah >= 10 and convertFah <= 17:
        print("It is mild out, wear a light jacket.")
    elif convertFah >= 17 and convertFah <= 29:
        print("It is warm outside.")
    elif convertFah >= 29 and convertFah <= 40:
        print("It is very hot! Drink some water and find some shade!")
    elif convertFah >= 40:
        print("We're melting!!!")
    
elif var == "fahrenheit" or "Fahrenheit" or "FAHRENHEIT" or "f" or "F":
    convertCel = (num - 32) * 5/9
    print("{} degrees fahrenheit = {} degrees celsius.".format(num, convertCel))
    if convertCel <= -40:
        print("Get inside and warm up! You will get hypothermia!")
    elif convertCel <= -40 and convertCel <= 10:
        print("It is cold, wear a warm jacket.")
    elif convertCel >= 10 and convertCel <= 17:
        print("It is mild out, wear a light jacket.")
    elif convertCel >= 17 and convertCel <= 29:
        print("It is warm outside.")
    elif convertCel >= 29 and convertCel <= 40:
        print("It is very hot! Drink some water and find some shade!")
    elif convertCel >= 40:
        print("We're melting!!!")