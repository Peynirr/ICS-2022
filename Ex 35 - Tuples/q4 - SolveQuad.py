# Omercan
# May 17 2022
# Ex 35 Q4
# Determining If We Can Calculate Real Roots

#Function
def verify(a, b, c):
    if type(a) == str or type(b) == str or type(c) == str:
            print("The values are not numbers")
            return (None, None)
    
    else:
        return solveQuad(a, b, c)
        

def solveQuad(a, b, c):
    #Discriminant
    discriminant = (b**2) - (4*a*c)
    
    if discriminant > 0:
        plus = (-b + discriminant**0.5) / (2*a)
        minus = (-b - discriminant**0.5) / (2*a)
        return (("({:.2}, {:.2})".format(plus, minus)))
    
    elif discriminant == 0:
        plus = (-b + discriminant**0.5) / (2*a)
        return ("({:.2}, {:.2})".format(plus, plus))
    
    else:
        print("There are no real root.")
        return (None, None)

#Call Functions
print(verify(1, 1, -4))
print(verify(1, 0, -4))
print(verify(1, 2, 1))
print(verify(6, 5, 7))
print(verify('a', 'b', 2))
