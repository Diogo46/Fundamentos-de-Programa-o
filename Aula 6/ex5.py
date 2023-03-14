import math

			
def floatInput(prompt,min=-math.inf,max=+math.inf):
	try:
		assert(min <= max)
	while True:
		res = input(prompt)
		try:
			res = float(res)
			if min < res < max:
				return res
			else:
				print(f'ERROR: Value should be in [{min}, {max}]')
		
		except ValueError:
			print('ERROR: Not a float!'	)
		
	except AssertionError:
		print('Invalid inetervale')

def main():
	print("a)")
	v = floatInput("Value? ")
	print("v:", v)
	
	print("b)")
	h = floatInput("Humidity (%)? ", 0,100)
	print("h:", h)
	
	print("c) Try entering invalid values such as 23C or -274.")
	t = floatInput("Temperature (Celsius)? ", min=-273.15)
	print("t:", t)

    #d) What happens if you uncomment this?
	impossible = floatInput("Value in [3, 0]? ", min=3, max=0)

	return

if __name__ == "__main__":
	main()
