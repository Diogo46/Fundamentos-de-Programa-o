def max2(n1,n2):
	maximo=n1
	if n2 > maximo:
		maximo = n2
	return maximo

def max3(x, y, z):
	maximo1 = max2(x, y)
	maximo2 = max2(y, z)
	return max2(maximo1, maximo2)
	
n1 = float(input('Um numero: '))
n2 = float(input('Um numero: '))
n3 = float(input('Um numero: '))

value_max = max3(n1, n2, n3)

print('O maior valor da função é {:.0f} '.format(value_max))

