# Write your solution here

def main():
	phonebook = {}
	selection = 0
	while selection != 3:

		selection = int(input("command (1 search, 2 add, 3 quit): "))

		if selection == 1 or selection == 2:
			name = input("name: ")
		if selection == 1:
			search(phonebook, name)
		if selection == 2:
			add(phonebook, name)

	print("quitting...")


def search(phonebook: dict, name: str):
	if name in phonebook:
		print(f"{phonebook[name]}")
	else:
		print("no number")


def add(phonebook: dict, name: str):
	number = input("number: ")
	phonebook[name] = number
	print("ok!")


main()