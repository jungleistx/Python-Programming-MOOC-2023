# Write your solution here

from string import ascii_lowercase
from random import randint

def generate_password(length:int) -> str:
	password = ''
	len_letters = len(ascii_lowercase)

	for i in range(length):
		index = randint(0, len_letters - 1)
		password += ascii_lowercase[index]
	return password


if __name__ == '__main__':
	for i in range(10):
		print(generate_password(8))


'''
	for i in range(length):
		password += choice(ascii_lowercase)
'''