# Write your solution here

def read_input(propmt:str, min:int, max:int) -> int:
	while True:
		try:
			number = int(input(str))
			if number >= min and number <= max:
				return number
		except ValueError:
			pass

		print(f'You must type in an integer between {min} and {max}')