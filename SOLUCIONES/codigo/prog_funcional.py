# prog. funcional
import random
from functools import reduce

def cuadrado(arg):
	return arg**2
	
#map: itera por los elementos de la lista
# aplicando la funcion cuadrado
L = list(range(10))
L2 = list(map(cuadrado, L))
print(L2)

# filter: filtra los elementos de la lista
# que cumplen una determina funcion ( si devuelve
# true el elemento se añade a la lista)
def par(arg):
	return True if arg % 2 == 0 else False
	
L3 = list(filter(par,L))
print(L3)

# Ejemplo List Compre. con el cuadrado de los 10 primeros
# numeros:
L2 = [i**2 for i in L]
print(L2)
L2 = [cuadrado(i) for i in L]
print(L2)

L2 = [(i,cuadrado(i)) for i in L]
print(L2)

print(chr(65))
print(ord('A'))

d1 = {i:i**2 for i in range(10)}
print(d1)

d2 = {chr(i):i for i in range(ord('A'),ord('Z')+1)}
print(d2)

for i in range(ord('A'),ord('Z')+1):
	print(chr(i),end=' ')
	
# Filter:
L3 = [i for i in range(10) if i % 2 == 0]
print('\n',L3)

'''
(1,1,1) ... (1,10,10), ... (5,1,5)(5,2,10) ...
'''
L=[(i,j,i*j) for i in range(1,11) for j in range(1,11)]
print(L)

L = [random.randint(1,100) for i in range(10)]
print(L)

'''
{'a':[34,67,55,44], 
 'b':[1,3,7,88]
'''
d1 = {chr(i):[random.randint(1,100) for i in range(10)] \
    for i in range(ord('A'),ord('F'))}
print("\n")
for k, L in d1.items():
	print(k, L)
	
print("_".join([str(i) for i in range(10)]))
print("_".join(['1','2','3','4']))

#reduce
def minimo(a,b):
	return a if a < b else b
	
L = [random.randint(1,100) for i in range(10)]
print(L)
num = reduce(minimo, L)
print(num, type(num))



L = [ (4,56,45), (8,8,230), (7,9,4) ]
# Ordenar DESC por el segundo valor de cada Tupla
L2 = sorted(L, key= lambda t : t[1], reverse=True)
print(L2)

# Ordenar ASC segun la suma de las componentes:
L2 = sorted(L, key= lambda t : sum(t))
print(L2)

# Devuelve el primer elemento de la lista:
cabeza = lambda L : L[0]

#Devuelve la lista quitando la cabeza:
resto = lambda L : L[1:]

L = list(range(10))
print(cabeza(L))
print(resto(L))











