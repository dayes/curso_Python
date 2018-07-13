# -*- coding: cp1252 -*-

"""SE UTILIZA UN DECORADOR PARA GRABAR INFORMACI�N EN UN LOG ASI EVITAMOS MODIFICAR LAS FUNCIONES ORIGINALES"""

"""Se realizan dos operaciones contra la BBDD y cada vez que se realice una hay que grabar en un log la fecha y la hora actuales, as�
como los datos de la operaci�n"""

import time

def log(metodo):
        def funcion(*args):                
                fecha = time.strftime("%d/%m/%y") # la fecha actual
                hora = time.strftime("%H:%M:%S")  # la hora actual
                sdatos = " ".join(args)
                linea = fecha + "  " + hora + "  operaci�n: " + metodo.__name__ + " Par�metros: " + sdatos + "\n"

                # grabar en el log:
                f = open("mi_log.txt","a")
                f.write(linea)
                f.close()
                #print linea # salida por consola

                # Llamar a la funci�n que recibe el decorador:
                metodo(*args)
        return funcion
        

@log
def grabar(user, password):
        """ Suponemos que hace un insert into en una tabla de usuarios de la BBDD"""
        print ("GRABAR datos en la BBDD " + user + " y " + password)

@log
def borrar(user):
        """Suponemos que hace un delete en una tabla de usuarios de la BBDD"""
        print ("BORRAR datos en la BBDD " + user)
   


# Cada vez que se realiza una operaci�n sobre la BBDD salta el decorador, OJO LAS FUNCIONES ANOTADAS CON EL NOMBRE DEL DECORADOR!!!
grabar("admin","1234")
borrar("admin")
