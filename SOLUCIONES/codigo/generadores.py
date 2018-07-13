# Generadores:
#De numeros primos:
from math import sqrt

def primos(ini, fin, salto=1):
	
	def esPrimo(numero):		
		for i in range(2, round(sqrt(numero))+1):
			if numero % i == 0:
				return False
		return True
		
	# Codigo principal del generador:
	i = ini
	while i < fin:
		if esPrimo(i):
			yield i
			
		i+=salto	
	
# Los primos del 200 al 300
L = [i for i in primos(200,300)]
print(L)
	

