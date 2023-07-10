# Write your solution here

from random import sample

def lottery_numbers(amount:int, lower:int, upper:int) -> list:
	number_pool = list(range(lower, upper + 1))
	selected_numbers = sample(number_pool, amount)
	selected_numbers.sort()
	return selected_numbers


if __name__ == "__main__":
	for number in lottery_numbers(7, 1, 40):
		print(number)