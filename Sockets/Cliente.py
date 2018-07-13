
import sys
import codecs
import socket
nombreFich = sys.path[0] + "/Contenido.txt"
s = socket.socket() 
s.connect(("localhost", 9999))


while True:
    with codecs.open(nombreFich, "r",encoding='utf-8', errors='ignore') as fdata:
        texto = fdata.read()
        s.send(texto.encode("utf-8")) 
    break
print ("adios")
s.close()