# Write your solution here
def palindromes(word : str) -> bool:

	length = len(word)
	if length > 0:
		index = length - 1
		for i in range(length):
			if word[i] != word[index]:
				return False
			index -= 1

	return True

# Note, that at this time the main program should not be written inside
# if __name__ == "__main__":
# block!

while True:

	word = input("Please type in a palindrome: ")

	if palindromes(word):
		print(f"{word} is a palindrome!")
		break
	else:
		print("that wasn't a palindrome")