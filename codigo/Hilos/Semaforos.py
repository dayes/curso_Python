# PRODUCTOR CONSUMIDOR
# CON N  -  M
from threading import Thread
from threading import Lock
from threading import Semaphore

import time, random

NUM_HUECOS = 20
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
            letra = chr(random.randint(65,65+25))
            self.semHuecos.acquire()    # Tenemos huecos
            # La R. C. es la lista. Exclusion mutua
            self.mutex.acquire()
            self.L.append(letra)
            print("Generada letra ",letra)
            print(self.L)
            self.mutex.release()
            self.semItems.release()     # Avisa de que tenemos un item
            #time.sleep(random.randint(0,2))
class Consumidor(Thread):
    def __init__(self, mutex, semHuecos, semItems, L):
        Thread.__init__(self)
        self.mutex = mutex
        self.semHuecos = semHuecos
        self.semItems = semItems
        self.L = L
    
    def run(self):
        for i in range(NUM_CHARS):
            self.semItems.acquire() #Espera a tener que consumir
            # La lectura tb en Exc. mutua
            self.mutex.acquire()
            letra = L.pop()
            self.mutex.release()

            self.semHuecos.release() #Avisa al productor que tiene huecos
            print("Consumidor: ", letra)
            #time.sleep(random.randint(0,2))


# código principal
# Semaforos
semHuecos = Semaphore(NUM_HUECOS)
semIems = Semaphore(0)
mutex = Lock()
L = []

p=Productor(mutex,semHuecos,semIems, L)
c = Consumidor(mutex,semHuecos,semIems, L)

p.start()
c.start()

p.join()
c.join()
