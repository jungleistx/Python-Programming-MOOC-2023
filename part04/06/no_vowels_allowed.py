# Write your solution here

def no_vowels(word: str) -> str:

	new_word = ""
	vowels = "aeiou"

	for char in word:
		if char not in vowels:
			new_word = new_word + char

	return new_word

if __name__ == "__main__":
	my_string = "this is an example"
	print(no_vowels(my_string))