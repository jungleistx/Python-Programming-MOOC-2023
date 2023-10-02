# Write your solution here:

from random import randint

def word_generator(characters:str, length:int, amount:int):
	for i in range(amount):
		word = ""
		for l in range(length):
			pos = randint(0, len(characters) - 1)
			word += characters[pos]
		yield word


if __name__ == "__main__":
	wordgen = word_generator("abcdefg", 3, 5)
	for word in wordgen:
		print(word)
