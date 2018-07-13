import sys

def sumar(a,b):
	return a+b
	
	
def restar(a,b):
	return a-b
	
	
L=["sumar","restar"]
modulo = sys.modules[__name__]


for f in L:
	# getattr necesita el modulo donde se encuentran las funciones
	# y en este caso estan en el mismo modulo si no hariamos:
	# import un_modulo
	# una_funcion = getattr(un_modulo, 'nombre_func')
	
	fn = getattr(modulo,f)
	print('Llamada a ', f, fn(1,2))
