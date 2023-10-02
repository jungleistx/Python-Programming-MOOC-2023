# Write your solution here

def all_the_longest(word_list: list) -> list:

	new_list = []
	longest = 0

	for word in word_list:
		current_len = len(word)
		if current_len > longest:
			longest = current_len

	for word in word_list:
		current_len = len(word)
		if current_len == longest:
			new_list.append(word)

	return new_list

