"""
Dada una frase obtener el número de ocurrencias de cada letra
"""
cadena = "Es un ejemplo de cadena"
histograma = dict()

for letra in cadena:
    if letra in histograma:
        histograma[letra] += 1
    else:
        histograma[letra] = 1
for k,v in histograma.items():
    print(k,v)

"""
Obtener los elementos comunes de dos listas en una tercera lista
"""
L1 = [4,6,3,7]
L2 = [2,3,1,4]
L3 = []
for elemento in L1:
    if elemento in L2:
        L3.append(elemento)
print(L3)