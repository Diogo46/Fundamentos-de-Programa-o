l = float(input('Quantidade de combustível em litros: '))
if l <= 40:
	p = l * 1.40
	print('O preço do combustível é {:.2f}'.format(p))
else:
	p = l * 1.40 * 0.90
	print('O preço do cumbistível é {:.2f}'.format(p))
	
