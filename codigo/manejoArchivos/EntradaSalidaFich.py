import sys
import codecs

class archivitos(object):
    def __init__(self, nombre="prueba.txt",texto=None):
        self.texto = texto
        self.nombre = nombre
    def guardar(self):
        fichero = open(self.nombre,"w")
        fichero.write(self.texto)
        fichero.close()

if __name__ == "__main__":
    nombreFich = sys.path[0] + "/Contenido.txt"
    particiones = int(input("Numero de partes: "))
    with codecs.open(nombreFich, "r",encoding='utf-8', errors='ignore') as fdata:
        texto = fdata.read()
        #print(texto)
        tamanoFich = len(texto)
        cadaParte = int(tamanoFich/particiones)
        print ("Las particiones son " + str(particiones) + " y quedan " + str(cadaParte))
        print("Generando Ficheros...")
        i = 0
        while i < particiones:
            archivo = archivitos("Contenido"+str(i)+".txt",texto[i*cadaParte:(i+1)*cadaParte])
            archivo.guardar()
            print("Contenido"+str(i)+".txt")
            print(texto[i*cadaParte:(i+1)*cadaParte])
            i += 3

