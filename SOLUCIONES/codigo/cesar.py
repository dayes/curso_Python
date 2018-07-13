alf = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 '

def codificarLetra(letra, alf):
	return alf.index(letra)
	
def decodificarLetra(numero, alf):
	return alf[numero]
		
def codificarCadena(cadena, alf):
	L = list()
	for i in cadena:
		L.append(codificarLetra(i, alf))
	return L
	
def decodificarCadena(L, alf):
	s = ''
	for i in L:
		s += decodificarLetra(i,alf)
	return s
	
def cifradoCesar(cadena, k, alf):
	'''
	Codificar la cadena en numeros
	A cada numero se le suma k
	decodificar la cadena, a partir de la lista de numeros
	'''
	L = codificarCadena(cadena, alf)
	L2 = []
	for i in L:
		ind = (i+k) % len(alf)
		L2 += [ind]
	return decodificarCadena(L2, alf)
	
def descifradoCesar(cadena, k, alf):
	return cifradoCesar(cadena, -k, alf)

cadena = 'HOLA QUE TAL'
s2 = cifradoCesar(cadena, 5, alf)
print(s2)
print(descifradoCesar(s2, 5, alf))
