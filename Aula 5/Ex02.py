def inputFloatlist():
	lista = []
	while True:
		a = input('Introduza um número: ')
		if a == '':
			return lista
		lista.append(int(a))

			
def countLower(lst, v):
	count = 0
	x = []
	for i in range(len(lst)):
		if v > lst[i]:
			x.append(lst[i])
			count += 1
	print(count, 'é o número de elementos inferiores a ', v)
	print('A lista de valores inferiores a ',v, 'é',x)

def minmax(lst):
	x = 0
	maximo = lst[0]
	minimo = lst[0]
	for i in range(1, len(lst)):
		if lst[i] > maximo:
			maximo = lst[i]
		if lst[i] < minimo:
			minimo = lst[i]
	print('O valor máximo da lista é ', maximo)
	print('O valor mínimo da lista é ', minimo)
	
	return [maximo,minimo]
	
def main():
	lst = inputFloatlist()
	cd = minmax(lst)
	maximo = cd[0]
	minimo = cd[1]
	media = (maximo+minimo)/2
	countLower(lst,media)
	print('A média entre max e min é ',media)
main()

	
	
	
