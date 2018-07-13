#-*- coding: cp1252 -*-
import socket


port = 9991
s = socket.socket()
#Reutilizar el socket:
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
s.bind(("localhost", port))
s.listen(1)

print ("Servidor a la espera en el puerto: " + str(port))
sc, addr = s.accept()

while True: 
	recibido = sc.recv(1024)
	recibido = recibido.decode('utf-8')
	if recibido == "quit": 
		break 
	print ("Recibido:", recibido)
	sc.send(recibido.encode('utf-8'))
        		
print ("Fin")
sc.close()
s.close()

