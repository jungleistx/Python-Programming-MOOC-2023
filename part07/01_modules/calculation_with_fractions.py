# Write your solution here

import fractions

def fractionate(amount:int) -> list:
	list_of_fractions = []
	if amount > 0:
		for x in range(amount):
			list_of_fractions.append(fractions.Fraction(1, amount))

	return list_of_fractions


if __name__ == "__main__":
	for p in fractionate(3):
		print(p)

	print()
	print(fractionate(5))