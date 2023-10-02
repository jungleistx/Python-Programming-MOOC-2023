# Write your solution here

def shortest(word_list : list) -> str:

	short = word_list[0]

	for word in word_list:
		if len(word) < len(short):
			short = word

	return short
