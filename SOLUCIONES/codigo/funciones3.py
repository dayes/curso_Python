'''
MENU
1. SUMAR
2. RESTAR
3. MULTIPLICAR
4. SALIR
OPCION: 
'''

def menu(L):
	num1 = int(input('Numero1:'))
	num2 = int(input('Numero2:'))
	
	while True:
		n=1
		print("MENU")
		for i in L:
			print(n,i.__name__)
			n+=1
		op = int(input('Dame opcion:'))
		
		if 1 <= op <= len(L):
			# Comprobar si la opcion es correcta
			if op == len(L):
				# ha pulsado salir
				L[op-1]()  # ojo, no tiene parametros
			else:
				# imprime el resultado y delante el nombre
				# de la funcion
				print(L[op-1].__name__,L[op-1](num1,num2))
		

def sumar(a,b):
	return a+b
	
def restar(a,b):
	return a-b
	
def multiplicar(a,b):
	return a*b
	
def salir():
	exit()

if __name__ == '__main__':
	# Este codigo solo se ejecuta cuando ejecutamos
	# pero cuando se importa el modulo no lo hace
	#porque la propiedad __name__ toma el valor funciones3
	# el nombre del modulo.
	L=[sumar, restar, multiplicar, salir]
	menu(L)
