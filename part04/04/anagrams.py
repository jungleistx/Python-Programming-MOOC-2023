# Write your solution here

def anagrams(word1 : str, word2 : str) -> bool:

	if len(word1) != len(word2):
		return False

	word1_sorted = sorted(word1)
	word2_sorted = sorted(word2)

	for i in range(len(word1)):
		if word1_sorted[i] != word2_sorted[i]:
			return False

	return True


if __name__ == "__main__'":
	anagrams("hello", "olleh")
	anagrams("hello", "moikk")