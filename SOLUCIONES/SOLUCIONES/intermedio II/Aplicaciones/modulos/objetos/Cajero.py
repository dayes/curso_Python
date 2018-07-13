from ..excepciones.CajeroException import *

class Cajero(object):
	def __init__(self, billetes):
        #Al inicializar el cajero le paso por parametros/diccionario los billetes que tiene. 
		#Se lo paso desde fuera, en este caso 100:5, 50:20, 20:20, 10:30
		self.__billetes=billetes

	def getBilletes(self):
		#Se devuelve una ref al Atributo
		return self.__billetes

	def getTuplaBilletes(self):                
                L=list(self.__billetes.keys())
                L.sort(reverse=True)
                LL=[]
                for i in L:
                        LL+=[self.__billetes[i]]
                return tuple(LL)
		
	def SacarDinero (self,importe):
		desglose={}
		if self.GetBalance() < importe:
			# Si no hay saldo suficiente lanzamos Excepcion
			raise CajeroException("No hay saldo suficiente en el cajero")
		else:
			L=list(self.__billetes.items())
			L.sort(reverse=True)
			
			for b,n in L:
				if importe >= 	b:
					numBilletes = importe // b
					importe = importe % b
					# Actualizar los billetes del cajero
					self.__billetes[b]-=numBilletes
					#Agregar el billete y la cantidad al desglose
					desglose[b]=numBilletes
		return desglose			
	       
        
	def IngresarDinero (self, billetes):
		"""Se recibe el importe a ingresar desglosado en billetes"""
		ingreso = 0
		for billete, cantidad in billetes.items(): #recorro el dicionario de lo que ingreso {50:1}
			self.__billetes[billete]+= cantidad #Voy al diccionario self.__billetes con la clave billete [50] y le sumo la cantidad.
			ingreso += billete * cantidad #Calculo la cantidad que he ingresado
		return ingreso

       
		
	def GetBalance (self):
		Importe = 0
		for billete, cantidad in self.__billetes.items(): #Voy recorriendo el diccionario y leo el billete y la cantidad que hay
			Importe += billete * cantidad
		return Importe

if __name__=='__main__':
	print (Cajero.GetBalance())
	print (Cajero.IngresarDinero ({50:1}))
	print (Cajero.IngresarDinero ({20:2, 10:3}))
	print (Cajero.SacarDinero (2300))
	print (Cajero.SacarDinero(440))
	print (Cajero.GetBalance())

                                                                                                  
    
