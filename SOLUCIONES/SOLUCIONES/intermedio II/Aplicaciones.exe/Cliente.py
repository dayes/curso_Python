class Cliente:

        def __init__(self, nombre, telefono, dni):
                self.__nombre = nombre
                self.__telefono = telefono
                self.__dni = dni

        def __str__(self):
                return self.__dni + " " + self.__nombre + " " + str(self.__telefono)


if __name__=="__main__":
        print ("Ejecucion del modulo")
