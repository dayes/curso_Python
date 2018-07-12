fich = "registros.doc.dat"
print(fich.count("."))
# buscar 1 punto
print(fich.index("."))
# buscar último punto (busqueda por la derecha)
print(fich.rindex("."))
# con find si no encuentra -1, con index excepcion

# Concatenar listas
L=list(range(10))
s = "**".join("hola")
print(s)
s="#".join(str(L))
print(s)

# buscar archivos
files = ["archivo.pdf","otro.pdf","mas.doc"]
for arch in files:
    t = arch.partition(".")
    if t[2] == "pdf":
        print (arch)

"""
Por consola siempre se puede pedir ayuda
help(list.append)
"""
