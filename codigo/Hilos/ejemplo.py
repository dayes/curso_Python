import threading, time
class MiThread(threading.Thread):
    def __init__(self, num): 
        threading.Thread.__init__(self) 
        self.num = num
    def run(self):
        for i in range(0,5):
            print ("Soy el hilo", self.num," con mensaje ",str(i))
            time.sleep(1)

print ("Soy el hilo principal")
L = []
for i in range(0, 10): 
    t = MiThread(i)
    t.start()
    L.append(t)    
for hilo in L:
    hilo.join()
