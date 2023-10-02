# Write your solution here

import json

def print_persons(filename:str):
	with open(filename) as file:
		data = file.read()

	people = json.loads(data)
	for person in people:
		name = person['name']
		age = person['age']
		hobbies = ', '.join(person['hobbies'])
		print(f'{name} {age} years ({hobbies})')


if __name__ == "__main__":
	print_persons('file1.json')
	print_persons('file2.json')
	print_persons('file3.json')
	print_persons('file4.json')