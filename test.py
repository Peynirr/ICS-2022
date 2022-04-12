count = 2 

while(count < 40): 
    if count % 10 == 0: 
        print()
    print("{:5}{:5}".format(count, count ** 2))
    count = count + 2