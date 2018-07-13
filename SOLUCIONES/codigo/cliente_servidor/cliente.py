import socket 

s = socket.socket() 
s.connect(("localhost", 9999)) 
print('Cliente conectado ...')

while True: 
	mensaje = input("> ") 
	s.send(mensaje.encode('utf-8')) 
	recibido = s.recv(1024) 
	recibido=recibido.decode('utf-8') 
	if mensaje == "quit": 
		break 

	print ("Recibido:", recibido ) 
	
print ("fin cliente" ) 
s.close() 
