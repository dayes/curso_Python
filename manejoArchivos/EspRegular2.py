"""
COD o S/N
_
3 vocales en MAY
_
6 números que no pueden empezar por 0
"""
import re

def validarCodigo(codigo):
    patron = "(COD|S/N)_[AEIOU]{3}_[1-9][0-9]{5}"
    
    if re.match (patron,codigo):
        return True
    else:
        return False

L=["COD_AUO_087987", "S/N_AEI_123456","COD_AEO_012345","CAD_ABC_654768","COD_abc_543543"]
L2 = [m for m in L if validarCodigo(m)]

print(L)
print(L2)