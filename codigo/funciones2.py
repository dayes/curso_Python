"""
Se pueden anidar
No acepta sobrecarga de funciones.
los parametros pueden tener valores por defecto, por lo que no son obligatorios
Una función es un objeto
"""
def mifuncion (texto, veces=1):
    pass
def funcion(p1,p2):
    return p1 ** p2

potencia = funcion(1,2)
print (potencia)

"""
Si se llama a un objeto oque no es una funcion error no calleble
"""
#numero = 5
#numero()

"""
Varios parametros, con número variable
"""
def otra (param1, *otros):
    """
    otros lo toma como una tupla. Con len miramos el tamaño
    """
    print("El paramentro es ", param1, " el resto: ")
    for i in otros:
        print(i, end=' ')
    
otra(2,5,4,"croquetas",2,1)

"""
Para pasar diccionarios con **
"""
def pasodict(**otros):
    if "path" in otros:
        print("Tengo path")
    for k,v in otros.items():
        print(k,v)

pasodict(path="c:", n=10)

"""
********** Practicas ***********
"""
#definir un diccionario con k: str y v:funciones
"""
MENU
1. SUMAR
2. RESTAR
3. MULTIPLICAR
4. SALIR
OPCION:
"""
def menu(L):
    for i in L:
        print(L)
    print("OPCION:")

def sumar(a,b):
    return a+b
def restar(a,b):
    return a-b
def multiplicar(a,b):
    return a*b
def operaciones(n1,n2,d):
    for k,v in d.items():
        print(k,v.__name__,v(n1,n2))

d = {"SUMAR":sumar, "RESTAR":restar, "MULTIPLICAR":multiplicar}
menu(d)
