### EJEMPLO USANDO GENERADORES
def binToDec(val):
    n = 0
    while val > 0:          
        yield (val % 2) * (2**n)
        val = val // 10
        n += 1
 
sum = 0
for val in binToDec(10011):
    print ("+", val, end=" ")
    sum += val
 
print ("=", sum)
