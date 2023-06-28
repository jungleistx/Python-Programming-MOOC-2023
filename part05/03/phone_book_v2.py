# Write your solution here

def main():
	phonebook = {}
	while True:
		selection = input("command (1 search, 2 add, 3 quit): ")
		if selection == '1':
			search(phonebook)
		if selection == '2':
			add(phonebook)
		if selection == '3':
			break

	print("quitting...")


def search(phonebook: dict):
	name = input("name: ")
	if name in phonebook:
		for number in phonebook[name]:
			print(number)
	else:
		print("no number")


def add(phonebook: dict):
	name = input("name: ")
	number = input("number: ")
	if name not in phonebook:
		phonebook[name] = []
	phonebook[name].append(number)
	print("ok!")


main()