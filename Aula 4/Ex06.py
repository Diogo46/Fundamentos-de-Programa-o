def leibnizPi4(N):
	total = 0
	for n in range(N):
		r = (-1)**n/(2*n + 1)
		total += r
		
	return total

n = int(input('Número de termos da soma: '))
print(leibnizPi4(n))
