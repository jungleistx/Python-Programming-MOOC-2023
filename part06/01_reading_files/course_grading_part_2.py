# wwite your solution here

def sum_of_list(numbers: list) -> int:
	total = 0
	for number in numbers:
		total += int(number)
	return total


def calculate_exercisepoints(exercises: int) -> int:
	points = exercises // 4		# every 10% (4) of the max 40 exercises grants 1 point
	return points


def calculate_grade(exam_score: int, exercises: int) -> int:
	points = calculate_exercisepoints(exercises)
	total = exam_score + points
	if total >= 0 and total <= 14:
		return 0
	elif total >= 15 and total <= 17:
		return 1
	elif total >= 18 and total <= 20:
		return 2
	elif total >= 21 and total <= 23:
		return 3
	elif total >= 24 and total <= 27:
		return 4
	elif total >= 28:
		return 5
	else:
		return -1


file_students = input("Student information: ")
file_exercises = input("Exercises completed: ")
file_exams = input("Exam points: ")

students = {}
exercises = {}
exam_scores = {}

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

with open(file_exams) as file:	# save the exam-scores to dict, id as key
	for line in file:
		line = line.replace('\n', '')
		line = line.split(';')
		if line[0] == 'id':
			continue
		exam_scores[line[0]] = sum_of_list(line[1:])

for key, value in students.items():
	if key in exercises and key in exam_scores:
		final_grade = calculate_grade(exam_scores[key], exercises[key])
		print(f"{value} {final_grade}")
