# Complete the code to make the HiLo game...

import random

def main():
    # Pick a random number between 1 and 100, inclusive
	secret = random.randrange(1, 101);
	print("Can you guess my secret?")
    # put your code here
	x = 0
	a = 'something'
	while a != 'U are right':
		i = int(input('The number you are thinking is: '))
		if i < secret:
			a = 'LOW'
		elif i == secret:
			a = 'U are right'
		else:
			a = 'HIGH'
		print(a)
		x += 1
	
	print('It took u ',x,' tries')


main()
