# Write your solution here

def factorials(n: int):
	numbers = {}

	i = 1
	total = 1
	while i <= n:
		numbers[i] = i * total
		total *= i
		i += 1

	return numbers
