import threading, time

itera = 100
contador = 0
contador2 = 0
mutex = threading.Lock()

def sumar(itera):
    global contador
    for i in range(itera):
        print(".")
        contador += 5 
def restar(itera):
    global contador
    for i in range(itera):
        print("-")
        contador -= 5

def sumarBloqueo(itera): 
    global contador2, mutex
    for i in range(itera):
        mutex.acquire()
        contador2 += 1
        mutex.release() 
    
def restarBloqueo(itera): 
    global contador2, mutex
    for i in range(itera):
        mutex.acquire()
        contador2 -= 1
        mutex.release()


hiloSum1 = threading.Thread(target=sumar(itera))
hiloDif1 = threading.Thread(target=restar(itera))
hiloSum2 = threading.Thread(target=sumarBloqueo(itera))
hiloDif2 = threading.Thread(target=restarBloqueo(itera))
time.sleep(2)
hiloSum1.start()
hiloDif1.start()
hiloSum2.start()
hiloDif2.start()

print("Fin de ejecución")
print("Contador sin bloqueo ", contador)
print("Contador con bloqueo ", contador2)
