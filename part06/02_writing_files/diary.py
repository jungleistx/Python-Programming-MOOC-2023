# Write your solution here

def add_entry(filename:str):
	text = input("Diary entry: ")
	with open(filename, 'a') as file:
		file.write(text + '\n')


def read_entries(filename:str):
	with open(filename) as file:
		text = file.read()
		print(text)


filename = 'diary.txt'

while True:
	print("1 - add an entry, 2 - read entries, 0 - quit")
	selection = input("Function: ")

	if selection == '0':
		break
	elif selection == '1':
		add_entry(filename)
	elif selection == '2':
		read_entries(filename)

print("Bye now!")