## Descargar un file:
try:
	import urllib2
	
except ImportError:
	import urllib.request as urllib2

url = "http://www.dpii.es/files/fich0.txt"
f = urllib2.urlopen(url)                
numero = int(f.read())
print (numero)
f.close()
