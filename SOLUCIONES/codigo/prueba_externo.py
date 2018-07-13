import sys

print(sys.path)
sys.path.append('C:\\modulos')

print()
print(sys.path)

import externo

externo.prueba()

print(sys.argv)
