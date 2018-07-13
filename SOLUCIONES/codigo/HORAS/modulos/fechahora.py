# clase FechaHora

try:
	from fecha import Fecha
except:
	from modulos.fecha import Fecha
	
try:
	from hora import Hora
except:
	from modulos.hora import Hora
	

# Con herencia Multiple		
class FechaHora(Fecha,Hora):
	
	def __init__(self, d=1,m=1,y=1970, h=0, M=0,s=0):
		Fecha.__init__(self, d,m,y)
		Hora.__init__(self,h,M,s)
		
	def __str__(self):
		return Fecha.__str__(self) + ' ' + Hora.__str__(self)
		
	def __repr__(self):
		return Fecha.__repr__(self) + ' ' + Hora.__repr__(self)
