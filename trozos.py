strin = "anananana"
n = 0
m = 3
pal = "ana"
veces = 0
for x in strin:
    if n <= (len(strin)-3) and m <= len(strin):
        if strin[n:m] == pal:
            veces += 1  
    n +=1
    m +=1   
print "La palabra", pal , "sale" , veces, "veces"
