# Imprimir mi propio fichero:

import sys

nombreFich = sys.argv[0]
f = None
f2 = None
print(nombreFich)
nombreFich2 = "copia de " + nombreFich
try:
	# abrir fichero
	f = open(nombreFich, "r") # Abrir para leer
	f2 = open(nombreFich2, "w") # Abrir para escribir
	
	while True:
		linea = f.readline()
		if not linea: break
		
		linea = linea.strip('\n')
		if len(linea) > 0:
			print(linea)
			f2.write(linea.upper()+'\n')
						
except IOError as e:
	print('Error:',e)
	
finally:
	if f != None:
		f.close()
	if f2 != None:
		f2.close()	
		
