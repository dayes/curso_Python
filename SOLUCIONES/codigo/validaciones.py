# expresiones regulares:
import re

def validarMatricula(matricula):
	patron = "^\d{4}[A-Z]{3}$"
	patron2 = "^\d{4}[^AEIOU]{3}$"
	if re.search(patron, matricula) and \
	re.search(patron2, matricula):
		return True
	else:
		return False
		
L = ['hola 4848TTG','5677','7888YYT','YHU','1234AER','5678HYT']
L2 = [m for m in L if validarMatricula(m)]

print(L)
print(L2)

patron = "^(\d{3})$|^(\d{8})$"
print(re.search(patron, '123'))

html="<table><tr><td>123</td><td>madrid</td></tr></table>"
patron = "<td>(.+)</td>"
mm=re.search(patron, html)
print(mm.group(0))

for match2 in \
re.finditer('<td.*?>(.*?)</td>', html,re.DOTALL):
	s = match2.group(1)
	print(s)


