# Omercan
# May 12 2022
# Ex 34 Q1
# Verify module

def isNumber(number):
    if type(number) == float or type(number) == int:
        return True
    elif type(number) == str:
        x = number

        if x[0] == '+' or x[0] == '-':
            temp = temp[1:]
        
        decimalDot = x.find('.')
        front = x[0:decimalDot]
        back = x[decimalDot + 1:]

        if decimalDot.isdigit() or front.isdigit() or front == "" and back.isdigit or back == "":
            return True
    return False