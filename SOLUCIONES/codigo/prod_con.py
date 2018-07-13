# PRODUCTOR - CONSUMIDOR
# CON N - M

from threading import Thread
from threading import Semaphore
from threading import Lock
import time, random

NUM_HUECOS = 10
NUM_CHARS = 30

class Productor(Thread):
	
	def __init__(self, mutex, semHuecos, semItems, L):
		Thread.__init__(self)
		self.mutex = mutex
		self.semHuecos = semHuecos
		self.semItems = semItems
		self.L = L
		
	def run(self):
		for i in range(NUM_CHARS):
			letra = chr(random.randint(65, 65+25))
			print('P: ', letra)
			
			self.semHuecos.acquire() # Tenemos huecos para escribir?
			
			# La R.C. es la lista, se escribe en Exclusión mutua
			self.mutex.acquire()
			self.L.append(letra)
			print(self.L)
			self.mutex.release()
			
			self.semItems.release() # Avisar de que tenemos un item
			
			time.sleep(random.randint(0,2))
			
			
class Consumidor(Thread):
	
	def __init__(self, mutex, semHuecos, semItems, L):
		Thread.__init__(self)
		self.mutex = mutex
		self.semHuecos = semHuecos
		self.semItems = semItems
		self.L = L
	
	def run(self):
		for i in range(NUM_CHARS):
			self.semItems.acquire() # Espera a tener letras
			
			# La lectura se hace en exclusion mutua:
			self.mutex.acquire()
			letra = self.L.pop()
			self.mutex.release()
			
			self.semHuecos.release() # Avisa al prod. que tiene huecos
			
			print("C: ", letra)
			time.sleep(random.randint(0,3))
			
			
	
# codigo principal:
# Semaforos:
semHuecos = Semaphore(NUM_HUECOS)
semItems = Semaphore(0)
mutex = Lock()
L = []

p = Productor(mutex, semHuecos, semItems, L)
c = Consumidor(mutex, semHuecos, semItems, L)

p.start()
c.start()

p.join()
c.join()


