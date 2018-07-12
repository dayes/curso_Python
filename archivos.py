# Imprimir el propio fichero
import sys
nombreFich = sys.argv[0]
print(nombreFich)
# Abrir fichero
f = None
try:
    f = open (nombreFich,"r") #Abre para leer
    while True:
        linea = f.readline()
        if not linea: break
        #if len(linea)>0:
        print(linea)
except:
    print("Error")
finally:
    if f != None:
        f.close()