#pruebas con funciones:

# definir un dict con k: str y v: funciones
'''
MENU
1. SUMAR
2. RESTAR
3. MULTIPLICAR
4. SALIR
OPCION: 
'''

def menu(L):
	pass

def sumar(a,b):
	return a+b
	
def restar(a,b):
	return a-b
	
def multiplicar(a,b):
	return a*b
	
def operaciones(n1, n2, d):
	for k,v in d.items():
		print(k, v.__name__, v(n1,n2))
	
d = {'sum':sumar,'dif':restar,'mul':multiplicar}

operaciones(4,5, d)



def funcion2(**params):
	
	if 'path' in params:
		print('Grabar en fichero')
		
	for k,v in params.items():
		print(k,v)
		

def funcion(p1,p2,*params):
	if len(params) > 0:
		if type(params[0])==str:
			print('El primer param es cadena')
			
	for i in params:
		print(i, end=' ')
	return p1 ** p2
	
	
potencia = funcion
print(potencia(3,4,88,5,6,7))

funcion2(path='c:\\docs',n=10)

numero = 5
# print(numero[0]) error no es indexable


