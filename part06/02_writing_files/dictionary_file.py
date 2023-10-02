# Write your solution here

def get_dictionary_content() -> dict:
	wordlist = {}
	with open('dictionary.txt') as file:
		for line in file:
			if len(line) > 0:
				line = line.replace('\n', '')
				line = line.split(';')
				wordlist[line[0]] = line[1]
	return wordlist


wordlist = get_dictionary_content()
while True:
	print('1 - Add word, 2 - Search, 3 - Quit')
	selection = input('Function: ')

	if selection == '1':
		word_fin = input("The word in Finnish: ")
		word_eng = input("The word in English: ")
		wordlist[word_fin] = word_eng
		with open('dictionary.txt','a') as file:
			file.write(f'{word_fin};{word_eng}\n')
		print('Dictionary entry added')

	elif selection == '2':
		search = input('Search term: ')
		for fin, eng in wordlist.items():
			if search in fin or search in eng:
				print(f'{fin} - {eng}')

	elif selection == '3':
		break

print('Bye!')