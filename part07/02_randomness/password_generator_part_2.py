# Write your solution here

from string import ascii_lowercase, digits
from random import choice, shuffle

def generate_strong_password(length:int, numbers:bool, special:bool) -> str:
	# has to contain atleast 1 lowercase letter
	letters = ascii_lowercase
	password = choice(letters)

	special_characters = '!?=+-()#'
	if special:
		password += choice(special_characters)
		letters += special_characters

	if numbers:
		password += choice(digits)
		letters += digits

	# fill the rest
	while len(password) < length:
		password += choice(letters)

	# randomize letters
	randomized_list = list(password)
	shuffle(randomized_list)
	randomized_password = ''.join(randomized_list)

	return randomized_password


if __name__ == '__main__':
	for i in range(10):
		print(generate_strong_password(8, True, True))