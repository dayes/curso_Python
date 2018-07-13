def union(L1,L2):
	L = list(set(L1) | set(L2))
	L.sort()
	return L
	
def interseccion(L1,L2):
	L = list(set(L1) & set(L2))
	L.sort()
	return L
	
def factorial(n):
	'''
	5! = 5 x 4 x 3 x 2 x 1  iterativa
	
	recursiva
	5! = 5 x 4!
	4! = 4 x 3!
	...
	1! = 1
	n! = n * (n-1)!
	'''
	return 1 if n == 1 else n * factorial(n-1)
	
	'''
	if n == 1:
		return 1
	else:
		return n * factorial(n-1)
	'''
	
def longitud(L):
	if L == []:
		return 0
		
	elif type(L[0]) == list:
		return longitud(L[0]) + longitud(L[1:]) 
	
	else:
		return 1 + longitud(L[1:])

if __name__ == '__main__':
	print(longitud([1,2,4,5,[7,9]]))

	print(factorial(90))

	L1 = [1,2,3,5,6,8,9,0,8,7,6]
	L2 = [6,5,8,7,7,3,2,9]

	print(union(L1,L2))
	print(interseccion(L1,L2))
