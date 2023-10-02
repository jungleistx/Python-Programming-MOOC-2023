# WRITE YOUR SOLUTION HERE:

from string import punctuation

def most_common_words(filename:str, lower_limit:int) -> dict:
	with open(filename) as file:
		content = file.read().strip().replace('\n', ' ')

		# remove punctuations from all content
		for letter in punctuation:
			content = content.replace(letter, '')

		words = content.split(' ')

		# save all words to a dict
		wordlist = {word: words.count(word) for word in words if len(word) > 0}

		# return words whose count >= limit
		return {word: count for word, count in wordlist.items() if count >= lower_limit}


if __name__ == "__main__":
	print(most_common_words("comprehensions.txt", 3))
	print(most_common_words("programming.txt", 3))
