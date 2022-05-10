#Test

def formatFloat (number, decimalPlaces, newLine):
    
    if (type(number) == float and type(decimalPlaces) == int and type(newLine) == bool):
      if newLine:
          print(("{:."+ str(decimalPlaces)+"f}").format(number))
      else:
          print(("{:."+ str(decimalPlaces)+"f}").format(number), end = "")
    else:
       print("The parameters are the incorrect type")
    
