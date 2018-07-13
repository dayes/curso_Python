# prueba con urllib2

import coordenadas
import json
import time
from urllib.request import urlopen

class GeoLocation(object):
	
	def getCoordenadas(self, ciudad, traza=False):
		try:			
			f = urlopen("http://maps.googleapis.com/maps/api/geocode/json?address="+ciudad + "&sensor=false&language=es")	
			contenido = f.read().decode('utf-8')
			
			if traza: print(contenido)
			dic = json.loads(contenido)
			
			if dic == None:
				return False
			
			latitud = float(dic["results"][0]['geometry']['location']['lat'])
			longitud = float(dic["results"][0]['geometry']['location']['lng'])
			
			if traza:
				print("***********************************")
				print('latitud', latitud)
				print('longitud', longitud)
				print("***********************************")
			f.close()
			
			return coordenadas.coordenadaGeo(latitud, longitud)
			
			
		except Exception as e:
			#print("ERROR:", e)
			return False
				
	
	
if __name__ == '__main__':
	try:
		L = ['Teruel', 'barcelona', 'paris','brasilia','oslo','benasque']
		location = GeoLocation()
		for i in L:
			coor = location.getCoordenadas(i)
			print(i, coor)
			time.sleep(0.5)
			
		
	except Exception as e:
		print('Error modulo principal:', e)
