import Call

class CallInternational(Call.Call):

        def __init__(self, fecha, hora, numero, tarifa, tiempo, roaming):
                Call.Call.__init__(self, fecha, hora, numero, tarifa, tiempo)
                self.__roaming = roaming

                        
        def __str__(self):
                return Call.Call.__str__(self) + " R: " + str(self.__roaming)

        def getImporte(self):
                return Call.Call.getImporte(self) + self.__roaming

if __name__=="__main__":
        print ("Ejecucion del modulo")
