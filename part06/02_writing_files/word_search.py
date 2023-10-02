# Write your solution here

def find_asterisks(search_term:str) -> list:
	wordlist = []

	with open('words.txt') as file:
		if search_term[0] == '*':
			for line in file:
				if line[:-1].endswith(search_term[1:]):
					wordlist.append(line[:-1])
		else:
			for line in file:
				if line.startswith(search_term[:-1]):
					wordlist.append(line[:-1])
	return wordlist


def find_dot(search_term:str) -> list:
	wordlist = []
	search_term_len = len(search_term)

	with open('words.txt') as file:
		for line in file:
			line = line[:-1]

			if len(line) == search_term_len:
				match = True
				for i in range(search_term_len):
					if search_term[i] == '.':
						continue
					elif search_term[i] != line[i]:
						match = False
						break
				if match:
					wordlist.append(line)
	return wordlist

def find_words(search_term:str) -> list:
	wordlist = []

	if '.' in search_term:
		wordlist = find_dot(search_term)
	elif '*' in search_term:
		wordlist = find_asterisks(search_term)
	else:
		with open('words.txt') as file:
			for line in file:
				line = line[:-1]
				if line == search_term:
					wordlist.append(line)

	return wordlist

# print(find_words('manitoba'))

# print(find_words("*vokes"))
# print(find_words("man*"))

# print(find_words(".a.e"))
# print(find_words("p.ng"))
