# Write your solution here

import random

def words(n:int, beginning:str) -> list:
	wordlist = []

	with open('words.txt') as file:
		for line in file:
			line = line.strip()
			if line.startswith(beginning):
				wordlist.append(line)

	if len(wordlist) < n:
		raise ValueError('Not enough matching words.')

	return random.sample(wordlist, n)


if __name__ == '__main__':
	word_list = words(3, "ca")
	for word in word_list:
		print(word)
