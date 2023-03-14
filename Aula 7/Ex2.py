with open('lusiadas.txt') as ficheiro:
	dicionario = {}
	for line in ficheiro:
		for caracter in line:
			if str.isalpha(caracter):
				letra = str.lower(caracter)
				if letra in dicionario:
					dicionario[letra] += 1
				else:
					dicionario[letra] = 1
	for key in sorted(dicionario.keys()):
		print('{} : {}'.format(key,dicionario[key]))
