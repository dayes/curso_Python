"""
Función para ordenar listas
"""
L1 = [5,4,3,2,9]
L1.sort()
print(L1)

# L.sort(key, reverse) -> dos parametros

L1.sort(reverse=True)
print(L1)

# solo el nombre de la función (el puntero), tiene que devolver un número.
L.sort(key=len) # ordena por la longitud de la cadena