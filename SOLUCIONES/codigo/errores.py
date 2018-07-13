# Excepciones

def convertir():
	print(int('455'))
	
def comprobar(arg=None):
	if arg==None:
		raise Exception("Parametro no puede ser None")
	else:
		print("comprobar: ",arg)

def dividir():
	a = 9
	b = 1
	print(a / b)
	convertir()

try:
	dividir()
	comprobar()
	#print(a())

except ValueError as e:
	print('El texto no es un numero:',e)
	
except ZeroDivisionError as e:
	print('error: ',e, e.__class__.__name__)
	
except Exception as e:
	print('error: ',e, e.__class__.__name__)

else:
	print('No hay error')
	
finally:
	print('finally')
	
print('mas instrucciones')
	
