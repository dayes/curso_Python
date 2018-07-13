#-*- coding: cp1252 -*-
import math

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


class Call(SMS):

        def __init__(self, fecha, hora, numero, tarifa, tiempo):
                SMS.__init__(self, fecha, hora, numero, tarifa)
                self.__tiempo = tiempo

        def __str__(self):
                return SMS.__str__(self) + " " + str(self.__tiempo) + " h."

        def getImporte(self):
                return SMS.getImporte(self) *  (self.__tiempo * 3600)


class CallInternational(Call):

        def __init__(self, fecha, hora, numero, tarifa, tiempo, roaming):
                Call.__init__(self, fecha, hora, numero, tarifa, tiempo)
                self.__roaming = roaming

                        
        def __str__(self):
                return Call.__str__(self) + " R: " + str(self.__roaming)

        def getImporte(self):
                return Call.getImporte(self) + self.__roaming
        

class Cliente:

        def __init__(self, nombre, telefono, dni):
                self.__nombre = nombre
                self.__telefono = telefono
                self.__dni = dni

        def __str__(self):
                return self.__dni + " " + self.__nombre + " " + str(self.__telefono)
        
class Factura:
        
        def __init__(self, fecha, numero, cliente):
                self.__cliente = cliente
                self.__numero = numero
                self.__fecha = fecha
                self.__detalles = []

        def __total(self):
                baseImpo = 0 
                for reg in self.__detalles:
                        baseImpo += reg.getImporte()
                        
                return baseImpo

        def __iva(self):
                return self.__total()*21/100

        def addDetalle(self, detalle):
                self.__detalles += [detalle]

        def generar(self):
                aux_total = self.__total()
                aux_iva = self.__iva()
                
                print ("Numero: ", self.__numero)
                print ("Fecha: ", self.__fecha)
                print ("Cliente: ", self.__cliente)
                print 

                for reg in self.__detalles:
                        print (reg, end=" ")
                        print (" --> ", reg.getImporte(), " eur")

                print ()
                print ("Base imponible: " + str(round(aux_total,2)) + " eur")
                print ("IVA: " + str(round(aux_iva,2)) + " eur")
                print ("TOTAL: ", round((aux_total+aux_iva),2)," eur")


# principal:
cli = Cliente("Juan Perez", 600998833, "56.777.888G")
fact = Factura("30/09/2016","16/0001",cli)
fact.addDetalle(SMS("1/09/2016","14:15",808585585,0.05))
fact.addDetalle(SMS("10/09/2016","08:09",608585445,0.05))
fact.addDetalle(SMS("12/09/2016","12:58",608564585,0.05))
fact.addDetalle(SMS("19/09/2016","14:15",208585585,0.05))

fact.addDetalle(Call("9/09/2016","14:15",208585585,0.025, 0.023))
fact.addDetalle(Call("19/09/2016","4:15",208585585,0.025, 0.08))
fact.addDetalle(Call("29/09/2016","16:15",208555585,0.025, 0.12))

fact.addDetalle(CallInternational("2/09/2016","09:15",208555585,0.025, 0.12, 1))

fact.generar()


                        



        
