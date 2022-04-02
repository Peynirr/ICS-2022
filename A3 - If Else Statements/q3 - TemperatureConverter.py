# a3 q3
# Temperature Converter
# Omercan
# March 10 2022
# ICS201

#input
print("Welcome to the temperature unit program!\n")
var = input("Please enter your unit of choice:\t")
num = int(input("Please enter a number of choice:\t"))

#process
if var == "fahrenheit" or "Fahrenheit" or "F" or "f":
    conCel = (num - 32) * 5/9
    print("{} degrees fahrenheit = {} degrees celsius.".format(num, conCel))
if var == "celsius" or "Celsius" or "C" or "c":
    conFah = (num * 9/5) + 32
    print("{} degrees celsius = {} degrees fahrenheit.".format(num, conFah))
    if conCel <= -40:
            print("Get inside and warm up! You will get hypothermia!")
    elif conCel <= -40 and conCel <= 10:
            print("It is cold, wear a warm jacket.")
    elif conCel >= 10 and conCel <= 17:
            print("It is mild out, wear a light jacket.")
    elif conCel >= 17 and conCel <= 29:
            print("It is warm outside.")
    elif conCel >= 29 and conCel <= 40:
            print("It is very hot! Drink some water and find some shade!")
    elif conCel >= 40:
            print("We're melting!!!")
else:
    if var == "celsius" or "Celsius" or "C" or "c":
        conFah = (num * 9/5) + 32
    if conFah <= -40:
        print("Get inside and warm up! You will get hypothermia!")
    elif conFah <= -40 and conFah <= 10:
        print("It is cold, wear a warm jacket.")
    elif conFah >= 10 and conFah <= 17:
        print("It is mild out, wear a light jacket.")
    elif conFah >= 17 and conFah <= 29:
        print("It is warm outside.")
    elif conFah >= 29 and conFah <= 40:
        print("It is very hot! Drink some water and find some shade!")
    elif conFah >= 40:
        print("We're melting!!!")