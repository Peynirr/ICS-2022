
width = 5
divisor = 1

for position in range(1, width): #1 to 4
   divisor = divisor * 10

remainder = int(763)

for position in range(width, 0, -1): #(5, 0, -1) => 5 to 1
   quotient = remainder // divisor
   print(width)
   remainder = remainder % divisor
   divisor = divisor // 10
   