#-*- coding: cp1252 -*-

def fibonacci(n):
        if n == 0:
                return 0
        elif n == 1:
                return 1
        else:
                return fibonacci(n-1) + fibonacci(n-2)


# FIBONACCI:
L=[fibonacci(i) for i in range(20)]
print (L)


#Combinaciones:
L1 = [3,2,1]
L2 = [5,6,4]

LL=[(i,j) for i in L1 for j in L2]
print ("L1: ",L1)
print ("L2: ",L2)
print ("LL: ",LL)

#Abecedario:
L=[chr(i+65) for i in range(26)]
print (L)

#A partir de un texto recuperar una lista con las palabras de 5 letras:
texto = """Dise�ar la factura de un operador de telefon�a. Donde se registran los SMS (fecha, numero destino, hora, tarifa), las llamadas (fecha, hora, numero destino, tarifa y tiempo de conexi�n en HORAS). y los datos del usuario. Considerar la posibilidad de que se efect�en llamadas internacionales donde se puede a�adir una cuota de roaming.  Los importes se calcular�n en base a unas tarifas, donde el SMS se tarifica por unidad, la llamada por SG. y a la llamada internacional se le a�ade una cuota de roaming.
En la factura se muestra la fecha, el n�mero de factura, datos del clientes y el desglose del consumo.
Se mostrar� la siguiente informaci�n"""

L=[i for i in texto.split(" ") if len(i)==5] 
print (L)








