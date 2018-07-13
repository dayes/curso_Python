from modulos.BBDD.CajeroBBDD import *

class CajeroAutomatico(object):

        def __init__(self):
                self.__cajeroBBDD = CajeroBBDD("modulos/BBDD/Banco.dat")                
                self.__cajero = self.__cajeroBBDD.cargar()

                
        def sacarDinero(self):

                try:
                        print ("Introduca importe a retirar:")
                        importe = int(input())

                        if importe % 10 != 0:
                                print ("El importe debe ser multiplo de 10")
                        else:
                                desglose=self.__cajero.SacarDinero(importe)
                                print ("Ha retirado:")
                                for b,c in desglose.items():
                                        print (c," billetes de ", b)
                                        
                        # Actualizar la BBDD
                        self.__cajeroBBDD.actualizar(self.__cajero)
                        
                except CajeroException as e:
                        print ("ERROR",e)

        def ingresarDinero(self):
                desglose = {}
                print ("Introduzca billetes")
                print ("100:3;50:1 ...")
                print ("Teclear:",)
                cadenasBilletes=input()
                billetes = cadenasBilletes.split(";")
                               
                for b in billetes:
                        t = b.partition(":")
                                                
                        billete = int(t[0])
                        cantidad = int(t[2])
                        desglose[billete]=cantidad
                        
                print (desglose)
                self.__cajero.IngresarDinero(desglose)

                # Actualizar la BBDD
                self.__cajeroBBDD.actualizar(self.__cajero)

        def consultarSaldo(self):
                print ("EL SALDO TOTAL DEL CAJERO:",end = " ")
                print (self.__cajero.GetBalance())
                
        def menu(self):
                while True:
                        try:
                                print ("\n\nSeleccione opcion:")
                                print ("1. Ingresar")
                                print ("2. Retirar")
                                print ("3. Saldo Cajero")
                                print ("4. Terminar")
                                print ("opcion:", end=" ")
                                op = int(input())
                                if op==1:
                                        self.ingresarDinero()
                                        
                                elif op==2:
                                        self.sacarDinero()
                                        
                                elif op==3:
                                        self.consultarSaldo()
                                        
                                elif op==4:
                                        break
                                else:
                                        print ("Introduzca opcion correcta")
                        except Exception as e:
                                print ("ERROR:",e)

                        
                        
#CODIGO PRINCIPAL                      
cajeroAutomatico = CajeroAutomatico()
cajeroAutomatico.menu()



		
		
		


	

	
