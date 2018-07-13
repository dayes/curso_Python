import threading

# variables globales
N = 1000000
contador = 0
contador2 = 0
mutex = threading.Lock()

def sumar():
	global contador
	for i in range(N):
		contador+=1
	
def restar():
	global contador
	for i in range(N):
		contador-=1
	
def sumarBloqueo():
	global contador2, mutex
	for i in range(N):
		mutex.acquire()
		contador2+=1
		mutex.release()
	
def restarBloqueo():
	global contador2, mutex
	for i in range(N):
		mutex.acquire()
		contador2-=1
		mutex.release()
		
hiloSum1 = threading.Thread(target=sumar)
hiloDif1 = threading.Thread(target=restar)
hiloSum2 = threading.Thread(target=sumarBloqueo)
hiloDif2 = threading.Thread(target=restarBloqueo)	

hiloSum1.start()
hiloDif1.start()
hiloSum2.start()
hiloDif2.start()


hiloSum1.join()
hiloDif1.join()
hiloSum2.join()
hiloDif2.join()


print("Fin de ejecucion")
print('Contador SIN BLOQUEO: ',contador)
print('Contador CON BLOQUEO: ',contador2)

	
