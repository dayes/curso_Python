#map
cuadrado=lambda x: x**2
cubo=lambda x: x**3

funciones = [cuadrado, cubo]
L=[1,2,3,4,5,6,7,8,9]

for f in funciones:
        print (list(map(f, L)))
        
#filter
multiplo8= lambda x: x % 8 == 0

print (list(filter(multiplo8, map(cubo, L))))



