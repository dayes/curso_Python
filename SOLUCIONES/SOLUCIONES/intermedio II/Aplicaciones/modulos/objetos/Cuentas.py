class CuentaBancaria(object):
	
	def __init__(self, iban, titular,saldo=100):
		self.__iban=iban
		self.__titular=titular
		self.__saldo=saldo
		
	def ingresar(self,cantidad):
		self.__saldo+=cantidad
		
	def retirar(self,importe):
		if self.__saldo >= importe:
			self.__saldo-=importe
		else:
			print ("No hay saldo suficiente")
			
	def consultarSaldo(self):
		return self.__saldo
		
#########################################################		
class CuentaAhorro(CuentaBancaria):
	
	def __init__(self,iban, titular,saldo=100,interes=2.5):
		#Desde el constructor de la clase hija llamar a la clase padre
		CuentaBancaria.__init__(self,iban,titular,saldo)
		self.__interes=interes
		
	def ingresar(self,cantidad):
		CuentaBancaria.ingresar(self,cantidad)
		if cantidad >= 1000:
			beneficio = cantidad * self.__interes / 100.0
			CuentaBancaria.ingresar(self,beneficio)

#########################################################				

class CuentaVivienda(CuentaBancaria):		
        def __init__(self,iban,titular,saldo=100,comision=2.5):
                CuentaBancaria.__init__(self,iban,titular,saldo)
                self.__comision=comision

        def retirar (self,importe):
                CuentaBancaria.retirar(self,importe)
                penalizacion = importe * self.__comision/100.0
                CuentaBancaria.retirar(self,penalizacion)

if __name__=='__main__':        
	cAhorro = CuentaAhorro("ES54-3000-9345-88-123456","JJ Gomez",450)
	print ("Saldo C.A:",cAhorro.consultarSaldo())
	cAhorro.ingresar(200)
	print ("Saldo C.A:",cAhorro.consultarSaldo())
	cAhorro.ingresar(1000)
	print ("Saldo C.A:",cAhorro.consultarSaldo())
	cVivienda = CuentaVivienda("ES54-3000-9345-88-123456","JJ Gomez",450)                                                                                                  
	print ("Saldo C.A:",cVivienda.consultarSaldo())
	cVivienda.retirar(1000)
	print ("Saldo C.A:",cVivienda.consultarSaldo())

