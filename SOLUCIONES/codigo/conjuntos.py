# conjuntos

comida = ['Ana','Jaime','Eva','Luis']
cena = ['Jaime','Alberto','Ruben','Eva']

co = set(comida)
ce = set(cena)

# Quien va a comer y a cenar:
print(co & ce)

# Quien va solo a comer:
print(co - ce)

# Quien va solo a cenar:
print(ce - co)

# Quien va solo a uno de los dos eventos:
print(co ^ ce)

# Quienes se han apuntado a alguno de los dos eventos:
print(co | ce)
