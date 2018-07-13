import re

# una validacion para billete:cantidad; ...

patron = "(500|200|100|50|20|10):[1-9][0-9]*"
cadena = "200:1"

if re.search(patron, cadena):
	print ("ok")
else:
	print ("NO")
