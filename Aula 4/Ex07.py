def maxmin():
	total = 0
	counter = 1
	
	while True:
		a = input('Introduza um número: ')
		if a == "":
			break     # if empty line, stop repeating
		v = float(a)
		x = total/counter
		if counter == 1:
			maximo = v
			minimo = v
		if v > maximo:
			maximo = v
		if v < minimo:
			minimo = v
		counter += 1
		total += v
	return maximo, minimo, x
		
	
	

print(maxmin())
