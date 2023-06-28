# Write your solution here

wordlist = []
word_count = 0

while True:
	word = input("Word: ")
	if word in wordlist:
		print(f"You typed in {word_count} different words")
		break
	word_count += 1
	wordlist.append(word)