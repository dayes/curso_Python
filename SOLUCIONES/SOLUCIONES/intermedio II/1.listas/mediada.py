# -*- coding: cp1252 -*-

#La mediana: de la lista de elementos ordenados es el punto medio:
L=[4,5,3,2,1,2,7,8,9,3,2,1]

L.sort()
n = len(L)

if n % 2 != 0:
        mediana = L[n/2]
else:
        #Tomar los dos elementos centrales y será la media de estos:
        mitad = n / 2
        e1 = L[int(mitad)]
        e2 = L[int(mitad-1)]
        mediana = (e1+e2)/2

print (L)
print ("La mediana sera: ", mediana)

