"""
Práctica de encriptar
1.- Función que códifica una letra
2.- Codificar la cadena, guardando en lista
"""
alf = " ABCDEFGHIJKLMNÑOPQRSTUVWXYZ0123456789"

def codificarLetra(letra, alf):
    return alf.find(letra)

def decodificarLetra(numero,alf):
    return alf[numero]

def codificarCadena(cadena, alf):
    L1 = []
    for x in cadena:
        L1.append(codificarLetra(x,alf))
    return L1
def decodificarCadena(L, alf):
    L1 = []
    for x in L:
        L1.append(decodificarLetra(x,alf))
    return L1

def cifradoCesar(cadena,k,alf):
    # Codificar cadena en números
    cifrado = codificarCadena(cadena, alf)
    # Cada número se suma k
    cifradoK = []
    #maximo = len(alf)
    for x in cifrado:
        ind = (x + k) % len(alf)
        cifradoK.append(ind)
    # Decodificar (convertir alf)
    return decodificarCadena(cifradoK,alf)
    

def descifradoCesar(cadena,k,alf):
    #codificar a numeros
    cifrado = codificarCadena(cadena, alf)
    #restar k
    cifradoK = []
    for x in cifrado:
        ind = x - k % len(alf)
        cifradoK.append(ind)
    # Decodificar (convertir alf)
    return decodificarCadena(cifradoK,alf)
    


cadena = "HOLA QUE TAL 8"
L = cifradoCesar(cadena,4,alf)
text = ""
for x in L:
    text += x
print(text)
text2 = ""
cadena2 = descifradoCesar(L,4,alf)
for x in cadena2:
        text2 += x
print(text2)
