'''
procesar formato json,

VISOR DE JSON: http://jsonviewer.stack.hu/
'''
import json

obj = {"menu":{"id": None,"valor":"Fichero","popup":{"menuitem":[{"id":"nuevo","value":"Nuevo Fichero"},
		{"id":"abrir","value":"Abrir Fichero"},{"id":"salir","value":"Salir del menu"}]}}}

print('Datos iniciales')
print(obj)
print('\nAcceso a obj:')
print('Campo valor: ', obj["menu"]["valor"])
print('menu de abrir: ', obj["menu"]["popup"]["menuitem"][1])

# El metodo dumps codifica en una cadena JSON: None se sustituye por null (en Json), True --> true / False --> false
datos = json.dumps(obj) # Recibe un objeto python y devuelve una cadena json
print('\nCodificado en json:')
print(datos)
print('\nCodificado en json pero con indentacion:')
print(json.dumps(obj, indent=4))

"""
El metodo dumps acepta todos estos objetos python para codificarlos en Json
Diccionarios (dict)
Listas y tuplas (list, tuple)
Cadenas (str en Python 3, unicode en Python 2)
Números (int, float)
True, False, y None
"""

#Decodificar una cadena escrita en Json y pasarlo a un objeto python se utiliza el metodo loads
datos2 = json.loads(datos) # loads recibe una cadena json y devuelve un objeto python
print('\nDecodificar json:')
print(datos2)

##################################
print('\nAcceso a la estructura:')
print('Campo valor: ', datos2["menu"]["valor"])
print('menu de abrir: ', datos2["menu"]["popup"]["menuitem"][1])

################################
# Se utiliza la funcion dump (opera con un archivo)
# Graba en un fichero la cadena json
with open("data.json", "w") as f:
	json.dump(obj, f)


# Se utiliza la funcion load (opera con un archvo)
# Recuperar de un fichero la cadena json en un objeto python
with open("data.json") as f:
	data = json.load(f)
	
print("\nResultado del fichero:")
print(data)
