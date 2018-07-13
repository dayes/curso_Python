# tipos iterables:
L = []
L2 = list()
L3 = list('hola que tal')
print(L,L2,L3)
L3 += [7]
print(L3)
print(L3 * 3)
print(type(L3))

for i in L3:
	print(i)
	
print(list(range(10)))

# Recorrer una lista con los indices:
for i in range(len(L3)):
	print(i, L3[i])

# slicing  [ini:fin-1:salto]
print(L3[::-1])
# el ultimo elemento de la lista:
print(L3[-1])
# Los 4 primeros elementos de la lista:
print(L3[0:4])
# los elementos pares de la lista:
print(L3[::2]) # saltos de dos en dos

# tuplas:
a,b,c = 3,4,5
print(a,b,c)

L = [(1,2), (3,4), (5,6)]
for i in L:
	print(i, type(i))

# explotar la tupla:
for a,b in L:
	print(a, b)
	
t = (1,2,3)
print(t[0])
# t[0] = 99 error la tupla es inmutable

t1 = (8)
print(type(t1))

t1 = 8,
print(type(t1))

# diccionarios:
d1 = dict()
d1['a'] = 445
d1['b'] = 566
print(d1)
print(d1.items())
for k, v in d1.items():
	print(k,v)

d2 = {0:[1,2,3], 1:[4,5,6] }
print(d2)

# Conjunto: para quitar repetidos:
L = list('hola que tal estas')
print(set(L))
L = list(set(L))

# operador de busqueda:
if 'h' in L:
	print('h existe')
else:
	print('h no existe')
	
# buscar en un dict:
if 'b' in d1:
	print('b existe')
else:
	print('b no existe')












