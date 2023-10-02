# Write your solution here

def store_personal_data(person:tuple):
	with open("people.csv", 'a') as file:
		line = f'{person[0]};{str(person[1])};{str(person[2])}'
		file.write(line + '\n')


# store_personal_data(("Paul Paulson", 37, 175.5))