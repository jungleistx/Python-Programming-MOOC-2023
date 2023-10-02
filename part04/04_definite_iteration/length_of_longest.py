# Write your solution here

def length_of_longest(word_list : list) -> int:

	longest = 0

	for word in word_list:

		wordlen = len(word)
		if wordlen > longest:
			longest = wordlen

	return longest