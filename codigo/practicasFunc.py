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
    print("Dame 1 número: ")
    n1 = int(input())
    print("Dame 2 número: ")
    n2 = int(input())
    
    print("MENU:")
    i=0
    for k in L:
        print(i, k.__name__)
        i += 1
    print("OPCION:")
    option = int(input())
    print(L[option](n1,n2))

def sumar(a,b):
    return a+b
def restar(a,b):
    return a-b
def multiplicar(a,b):
    return a*b
def salir():
    exit()

L = [sumar, restar, multiplicar, salir]
menu(L)
