# -*- coding: cp1252 -*-
import math

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
