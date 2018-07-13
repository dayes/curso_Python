# codigo principal
from modulos.fechahora2 import FechaHora2
from modulos.fechahora import FechaHora
from modulos.fecha import Fecha
from modulos.hora import Hora


f3 = FechaHora2()
print(f3)

f3 = FechaHora2(hora = Hora(5,6,7))
print(f3)

f3 = FechaHora2(h=5,M=6,s=7)
print(f3)

f2 = FechaHora(s = 40)
print(f2)

f1 = Fecha()
print(f1)

h1 = Hora(3)
h2 = Hora(1,1,1)
h3 = Hora(8,30)
h4 = Hora(4,55,6)

h1()

if h1:
	print('h1 es true')
else:
	print('h1 false')

L = [h1,h2,h3,h4]
L.sort(reverse=True)

r = h1 + h2
print(r)
print(L)
	

