# tamaño de un archivo:
import os

print(os.listdir())

tam_bytes = os.path.getsize('contenido.txt')
print(tam_bytes)

bytes_ = tam_bytes // 10
f = open("contenido.txt", "r")
i = 1

while True:
	texto = f.read(bytes_)
	if not texto: break
	nombre = "parte_" + str(i) + ".txt"

	f2 = open(nombre, "w")
	f2.write(texto)
	f2.close()
	i+=1
f.close()
