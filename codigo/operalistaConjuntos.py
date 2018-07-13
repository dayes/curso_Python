"""
"""
comida = ["ana", "david", "eva"]
cena = ["david", "jaime"]
co = set(comida)
ce = set(cena)

#Quien va a comer y cenar
print(co & ce)
#Quien va solo a comer
print(co - ce)
#Quien va solo a cenar
print(ce - co)
#Quien va solo a uno de los dos eventos
print(co ^ ce)
# Quien se ha apuntado a alguno de los dos eventos
print(co | ce)