# write your solution here

with open("wordlist.txt") as file:

	words = file.read()
	words = words.split('\n')

	user_text = input("Write text: ")

	user_text = user_text.split(' ')

	for word in user_text:
		if word.lower() in words:
			print(word, end=' ')
		else:
			print(f"*{word}* ", end='')

	print()