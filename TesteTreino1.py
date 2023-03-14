def inputFloatList():
	lista = []
	while True:
		number = input('Insira um numero: ')
		if number == '':
			return lista
		lista.append(int(number))
	
def countLower(lst,v):
	counter = 0
	x = []
	for i in range(len(lst)):
		if v > lst[i]:
			x.append(lst[i])
			counter += 1
	return counter
	
def minmax(lst):
	s = 0
	maximo = lst[0]
	minimo = lst[0]
	for i in range(1,len(lst)):
		if lst[i] > maximo:
			maximo = lst[i]
		if lst[i] < minimo:
			minimo = lst[i]
			
	return [maximo, minimo]
	
def main():
	lst = inputFloatList()
	cd = minmax(lst)
	maximo = cd[0]
	minimo = cd[1]
	media = (cd[0]+cd[1])/2
	countLower(lst,media)
	print('A média entre max e min é ',media)
main()
