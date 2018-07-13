# codigo del Servidor:
import socket 

s = socket.socket() 

# Para reutilizar el puerto, si se queda colgado:
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
s.bind(("localhost", 9999)) 
s.listen(1) 

print("Servidor creado, a la espera de clientes")
sc, addr = s.accept() 

print("Cliente aceptado ...")

while True: 
	recibido = sc.recv(1024) 
	recibido=recibido.decode('utf-8') 
	if recibido == "quit": 
		break
		
	print ("Recibido:", recibido) 
	mensaje = input("Server>")
	sc.send(mensaje.encode('utf-8'))
	
print ("fin comunicación servidor") 
sc.close() 
s.close()
