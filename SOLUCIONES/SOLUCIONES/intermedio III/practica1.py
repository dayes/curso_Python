import random

print("num intervalos:")
numint = int(input())
print("num max:")
nummax = int(input())

n = nummax // numint
print(n)
L= list() # =[]
ini=0
fin=n-1
for i in range(numint):
	t = (ini,fin)
	L.append(t)
	ini += n
	fin += n
print(L)


clasificador = dict()
for i in range(10):
	# generar num aleatorio
	numale =random.randint(0,nummax-1)
	# buscar en la lista la tupla que lo contiene
	for a,b in L:
		#print("tupla:",a,b,numale, type(a),type(b),type(numale))
		if a <= numale <= b:
			# y con la tupla acceder al clasificador para añadir el numero:
			if (a,b) not in clasificador:
				clasificador[(a,b)]=[numale]
			else:
				clasificador[(a,b)].append(numale)
			break
	
print(clasificador)	
	
	

