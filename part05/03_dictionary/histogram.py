# Write your solution here

def histogram(word: str):

	initials = {}

	for letter in word:
		if letter not in initials:
			initials[letter] = 0
		initials[letter] += 1

	for key, value in initials.items():
		print(f"{key} {value * '*'}")


if __name__ == "__main__":

	histogram("abba")