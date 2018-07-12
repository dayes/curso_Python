import re

def validarMatricula(matricula):
    patron = "[0-9]{4}[A-Z]{3}"
    if re.match (patron,matricula):
        return True
    else:
        return False

L=["4848FTJ", "788YYT","YHU","1234AER","5566.HYT"]
L2 = [m for m in L if validarMatricula(m)]

print(L)
print(L2)