"""Clase coordenada para calculos geograficos"""

class posicion(object):
	
	def __init__(self, grado, tipo):
		if tipo == 'Lat':
			self.__dir = 'N' if grado > 0.0 else 'S'
			
		if tipo == 'Long':
			self.__dir = 'E' if grado > 0.0 else 'W'
			
		self.__g = abs(int(grado))
		parteDecimal = abs(grado - int(grado))
		minutos = parteDecimal * 60.0
		self.__m = int(minutos)
		segundos = (minutos - self.__m) * 60.0
		self.__s = int(segundos)
		
	def toDouble(self):
		val = self.__g + self.__m / 60.0 + self.__s / 3600
		val = val * -1 if self.__dir == 'S' or self.__dir == 'W' else val
		return val

	def __str__(self):
		return str(self.__g) + "º " + str(self.__m) + "'" + str(self.__s) + "\" " + self.__dir

class coordenadaGeo(object):
	
	def __init__(self, lat, lon):
		self.__pos = (posicion(lat, 'Lat'), posicion(lon, 'Long'))
		
	def antipodas(self):
		pass
		
	def contenida(self, coordenada1, coordenada2):
		pass
		
	def latitud(self):
		return self.__pos[0]
		
	def longitud(self):
		return self.__pos[1]
		
	def __str__(self):
		return str(self.__pos[0])+ "  " + str(self.__pos[1])
		

if __name__ == '__main__':
	madrid = coordenadaGeo(40.4, -3.6875)
	print('Madrid', madrid)
	print(madrid.latitud().toDouble())
	print(madrid.longitud().toDouble())
		
