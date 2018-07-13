import re

def validacion(cadena, patron):
                
        if re.match(patron, cadena):
                return True
        else:
                return False


cadenas = ["COD_AEE_800959","COD_AEE_000959","COD_ABE_800959","SN_AEE_800959","S/N_AEC_000959"]
cadenas = ["COD_AAE_123456","S/N_AI_123456","COD_aae_123456","S/N_UUy_889977"]

print ("Validaciones:")
patron = "(S/N|COD)_[AEIOU][AEIOU][AEIOU]_[1-9][0-9]{5}"

for s in cadenas:
        print (s, validacion(s, patron))

        
