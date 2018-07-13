#operadores:

'''
A nivel de  bits
1000 1010
<< 2 multiplica por 2(elevado al numero de bits)

0010 1000


1000 1010
>> 1
0100 0101
dividir por 2(elevado al numero de bits)

~
1111 0000
0000 1111
'''
numero = 32
print(bin(numero))
# modificar el bit 1, cambiamos a 1
numero = numero | (1<<1)
print(bin(numero))
# cambiar el  bit 5 a 0:
'''
0010 0010
0010 0000 -> ~1101 1111
&
0010 0010
1101 1111
0000 0010
'''
numero = numero & ~(1<<5)
print(bin(numero))




