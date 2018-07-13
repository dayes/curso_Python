# Desplazamienkto de bit
# 1000 1010
# << 2
"""
0010 1000
Como multiplicar por 2
"""
desplaza = 32
print (bin(desplaza))
# modificar el bit 1
desplaza = desplaza | (1<<1)
print (bin(desplaza))
deplaza = desplaza & ~(1<<5)
print(bin(desplaza))


