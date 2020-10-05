result = False
while not result :
    melon_weight = input ("Give melon weight")
    if melon_weight >= 1 and melon_weight <= 100 :
        if melon_weight % 2 > 0 :
            print ("No")
        else :
            print ("Yes")
        result = True
    else :
        print ("Give a weight between 1 and 100")
        
