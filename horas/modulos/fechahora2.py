# FechaHora2
from modulos.fecha import Fecha
from modulos.hora import Hora
# Con Composicion:	
class FechaHora2:
	
	'''
	def __init__(self, fecha = Fecha(), hora = Hora()):
		self.fecha = fecha
		self.hora = hora
	'''
	def __init__(self, fecha = None, hora = None, \
	d=1,m=1,y=1970, h=0, M=0,s=0):
		if fecha == None:
			self.fecha = Fecha(d,m,y)
		else:
			self.fecha = fecha
			
		if hora == None:
			self.hora = Hora(h,M,s)
		else:
			self.hora = hora
	
	def __str__(self):
		return str(self.fecha) + ' ' + str(self.hora)
		
	def __repr__(self):
		return repr(self.fecha) + ' ' + repr(self.hora)
