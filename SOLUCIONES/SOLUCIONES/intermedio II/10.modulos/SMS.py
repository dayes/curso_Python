class SMS:

        def __init__(self, fecha, hora, numero, tarifa):
                self.__fecha = fecha
                self.__hora = hora
                self.__numero = numero
                self.__tarifa = tarifa
               

        def __str__(self):
                return str(self.__fecha) +" "+ str(self.__hora)+" "+str(self.__numero)+" "+str(self.__tarifa)

        def getImporte(self):
                return self.__tarifa


if __name__=="__main__":
        print ("Ejecucion del fuente")
