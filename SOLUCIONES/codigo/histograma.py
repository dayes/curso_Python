# Dado una frase obtener el numero de ocurrencias 
# de cada letra:

s= 'Dado una frase obtener el numero de ocurrencias de cada letra'
histograma = dict()

for letra in s:
	# La letra ya existia:
	if letra in histograma:
		histograma[letra] += 1
	else:
		# la primera vez que aparece  la letra:
		histograma[letra] = 1

# Ordenar DESC el dict. segun los valores
histograma = dict(sorted(histograma.items(), key=lambda t:t[1], reverse=True))
		
for k,v in histograma.items():
	print(k,v)
