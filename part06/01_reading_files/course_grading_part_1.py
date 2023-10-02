# write your solution here

def sum_of_list(numbers: list) -> int:
	total = 0
	for number in numbers:
		total += int(number)
	return total


file_students = input("Student information: ")
file_exercises = input("Exercises completed: ")

students = {}
exercises = {}

with open(file_students) as file:	# save the students name to dict, id as key
	for line in file:
		line = line.replace('\n', '')
		line = line.split(";")
		if line[0] == 'id':
			continue
		students[line[0]] = line[1] + ' ' + line[2]

with open(file_exercises) as file:	# save the exercises to dict, id as key
	for line in file:
		line = line.replace('\n', '')
		line = line.split(';')
		if line[0] == 'id':
			continue
		exercises[line[0]] = sum_of_list(line[1:])

for key, value in students.items():
	if key in exercises:
		print(f"{students[key]} {exercises[key]}")
