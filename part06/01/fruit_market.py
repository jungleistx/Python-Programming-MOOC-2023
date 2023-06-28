# write your solution here

def read_fruits() -> dict:
	fruits = {}

	with open("fruits.csv") as file:

		for line in file:
			line = line.replace("\n", "")
			items = line.split(";")
			fruits[items[0]] = float(items[1])

	return fruits
