import random


errores = 0 
for i in range(1,32000):
        try:
                a = random.randint(1,100)
                b = random.randint(1,100)

                r = 12345 / (a - b)
                
        except:
                errores += 1

print ("Errores: ", errores)


