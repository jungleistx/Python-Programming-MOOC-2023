# Write your solution here

def no_shouting(word_list: list) -> list:

	new_list = []

	for word in word_list:
		if not word.isupper():
			new_list.append(word)

	return new_list