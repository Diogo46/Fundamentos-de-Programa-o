def countdown(N):
	if N > 0:
		print(N)
		countdown(N-1)
	if N <= 0:
		print('ERROR')
		exit(1)
		
		
N = int(input('N: '))

countdown(N)
