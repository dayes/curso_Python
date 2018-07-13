class ARJ:

        def __init__(self, fichero, n=5):
                self.__fichero = fichero
                self.__n = n

        def __grabarFich(self,nombre,texto):
                f = open(nombre, "w")
                f.writelines(texto)
                f.close()

        def go(self):
                #Parte el fichero en las n particiones
                f = open(self.__fichero, "r")
                lineas = f.readlines()
                texto = "".join(lineas)

                nTexto = len(texto) // self.__n

                print ("Informe:")
                print ("Fichero: ",self.__fichero)
                print ("NumChars Total:",len(texto))
                print ("Particiones: ", self.__n)
                print ("NumChars Particion:", nTexto)
                print ("\nGenerando ficheros ...")

                nombre=self.__fichero.split(".")[0]
                ext = self.__fichero.split(".")[1]
                index=0
                for i in range(self.__n):
                        nombre2 = nombre + "_" + str(i) + "." + ext
                        print (nombre2)

                        if i+1 == self.__n:
                                # Coje hasta el final                                
                                auxText = texto[index:]
                        else:
                                auxText = texto[index:index+nTexto]
                    
                        index+=nTexto
                        self.__grabarFich(nombre2, auxText)
                        
               
                f.close()



try:
        arj = ARJ("Contenido2.txt", 4)
        arj.go()
        
except Exception as e:
        print (e)
