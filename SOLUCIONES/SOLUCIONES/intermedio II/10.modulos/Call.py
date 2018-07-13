import SMS

class Call(SMS.SMS):

        def __init__(self, fecha, hora, numero, tarifa, tiempo):
                SMS.SMS.__init__(self, fecha, hora, numero, tarifa)
                self.__tiempo = tiempo

        def __str__(self):
                return SMS.SMS.__str__(self) + " " + str(self.__tiempo) + " h."

        def getImporte(self):
                return SMS.SMS.getImporte(self) *  (self.__tiempo * 3600)


if __name__=="__main__":
        print ("Ejecucion del fuente")
