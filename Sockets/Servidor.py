import sys
import codecs
import socket

s = socket.socket() 
s.bind(("localhost", 9999)) 
s.listen(1)
sc, addr = s.accept()

while True:
    recibido = sc.recv(1024)
    recibido=recibido.decode("utf-8") 
    fichero = open("Recibido.txt","w")
    fichero.write(recibido)
    fichero.close()
    break
print ("fin comunicación") 
sc.close()
s.close()