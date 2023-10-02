# Write your solution here

def is_prime(number:int) -> bool:
	# added for reusability. From prime_numbers() number is always >= 2
	if number < 2:
		return False

	for i in range(2, number):
		if number % i == 0:
			return False
	return True


def prime_numbers():
	number = 2
	while True:
		if is_prime(number):
			yield number
		number += 1


if __name__ == "__main__":
	numbers = prime_numbers()
	for i in range(8):
		print(next(numbers))