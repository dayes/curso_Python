# pruebas con iterables:
d = {'a':1, 'b':2, 'c':3}
d2 = {'b':22,'c':33, 'd':4,'e':5}

d.update(d2)
del d['a']
print(d)

L = [1,2,3,4]
#L2 = L ojo, es una ref a los mismos datos
L2 = L.copy() # Crea una copia independiente
L2[0] = 1000
print(L)

# cadenas:
fich = "registros.doc.dat"
print(fich.count('.'))

# buscar el primer punto:
print('Con index: ', fich.index('.'))
# el ultimo:
print('Con rindex: ', fich.rindex('.'))

print('Con find: ', fich.find('.'))
# el ultimo:
print('Con rfind: ', fich.rfind('x'))

L=list(range(10))
s = "**".join("hola")
print(s)

n = 10
print("n " + str(n))

L = ['cv.pdf','carta.docx','programa.exe']
for f in L:
	t = f.partition('.')
	if t[2] == 'pdf':
		print(f)
		
# obtener las palabras de un texto:
s= 'Dado una frase obtener el numero de ocurrencias de cada letra'
L = s.split(' ')
for i in L:
	print(i)
	
s2 = s.replace(' ','')
print(s2)
print(s)

L = [1,2,3]
print(L.append(4))

s = "hola"
print(s.upper())

L1 = [1,2,3,4]
L2 = [1,2,3,4]
if L1 == L2:
	print('Son iguales')
else:
	print('distintas')
	
L = [1,4,3,-4,6,5,4,4,33,32,11]
L.sort()
print(L)

L.sort(reverse=True)
print(L)

L = ['zzza','x','555','aabb','nhn']
L.sort()
print(L)

# ordenar por la longitud de la cadena:
L.sort(key=len, reverse=True)
print(L)


	









