# Write your solution here

import difflib

def main():
	text = input('write text: ')
	words = text.split(' ')

	wordlist = get_wordlist()

	suggestions = {}
	for word in words:
		if word.lower() not in wordlist:
			print(f'*{word}*', end=' ')
			suggestions[word] = get_suggestions(word, wordlist)
		else:
			print(word, end=' ')
	print()

	if len(suggestions) > 0:
		print('suggestions:')
		for orig_word, sug_words in suggestions.items():
			print(f'{orig_word}: ', end='')
			words = ', '.join(sug_words)
			print(words)


def get_wordlist() -> list:
	wordlist = []
	with open('wordlist.txt') as file:
		for line in file:
			wordlist.append(line.strip())
	return wordlist


def get_suggestions(word:str, wordlist:list) -> list:
	suggestions = difflib.get_close_matches(word, wordlist)
	return suggestions


main()