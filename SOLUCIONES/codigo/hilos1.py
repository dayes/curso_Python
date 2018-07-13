# Ejemplo de hilos:

import threading, time

class Hilo(threading.Thread):
	
	def __init__(self, nombre):		
		# Llamar al constructor de la clase Padre:
		threading.Thread.__init__(self)
		self.nombre = nombre
		
	def run(self):
		# Est metodo se ejecuta al llamar a start() sobre un hilo.
		for i in range(5):
			print("Mensaje: " + self.nombre + " N" + str(i))
			#time.sleep(2)
		print('Termina ' + self.nombre + " quedan " + \
		str(threading.activeCount()))
		
# codigo principal:
# Crear varios hilos y se ponen en funcionamiento con start
L=[]
for i in range(5):
	nombre = "hilo " + str(i)
	h = Hilo(nombre)
	h.start()  # Se ejecuta el metodo run()
	L.append(h)
	
for hilo in L:
	hilo.join()
	
