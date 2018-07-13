def todos_iguales(A, ele, actual):
	"""
	lista, objeto, int -> bool
	OBJ: comprueba si todos los elementos de una lista son iguales a uno dado
	PRE: La lista debe contener al menos un elemento
	"""
	if (actual == len(A)-1):
		result = (A[actual] == ele)
	else:
		result = (A[actual] == ele) and (todos_iguales(A,ele,actual+1))
	return result
	
	
# Prueba
L = [1,1,1,1,1]
print(todos_iguales(L,1,0)) # Debe mostrar True
L2 = [1,2,3,1,1]
print(todos_iguales(L2,1,0)) # Debe mostrar False


print(todos_iguales.__class__)
print(todos_iguales.__dict__)
