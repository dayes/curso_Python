# Un retorno
def sumar(a,b):
    return a+b
# Varios retornos
def sumaResta(a,b):
    return a+b, a-b
n = sumar(5,3)
print(n)
s,r = sumaResta(5,3)
print(s,r)