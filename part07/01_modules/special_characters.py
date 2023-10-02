# Write your solution here

import string

def separate_characters(my_string:str) -> tuple:
	letters = ''
	punctuations = ''
	others = ''

	for letter in my_string:
		if letter in string.ascii_letters:
			letters += letter
		elif letter in string.punctuation:
			punctuations += letter
		else:
			others += letter

	return (letters, punctuations, others)


if __name__ == "__main__":
	parts = separate_characters("Olé!!! Hey, are ümläüts wörking?")
	print(parts[0])
	print(parts[1])
	print(parts[2])