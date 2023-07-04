# tee ratkaisu tänne

def sum_of_list(numbers: list) -> int:
	total = 0
	for number in numbers:
		total += int(number)
	return total


def calculate_exercisepoints(exercises: int) -> int:
	return exercises // 4		# every 10% (4) of the max 40 exercises grants 1 point


def calculate_grade(exam_score: int, exercises: int) -> int:
	points = calculate_exercisepoints(exercises)
	total = exam_score + points
	if total <= 14:
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


def build_coursename(filename:str) -> str:
	course_name = ''
	with open(filename) as file:
		for line in file:
			line = line.replace('\n', '')
			line = line.split(': ')
			course_name += line[1] + ', '
		course_name = course_name[:-2]
		course_name += ' credits'
	return course_name


file_students = input("Student information: ")
file_exercises = input("Exercises completed: ")
file_exams = input("Exam points: ")
file_course = input("Course information: ")
coursename = build_coursename(file_course)

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

with open('results.txt', 'w') as file_txt, open('results.csv', 'w') as file_csv:
	file_txt.write(coursename + '\n')
	underscore = len(coursename)
	file_txt.write(underscore * '=' + '\n')
	file_txt.write(f"{'name':30}{'exec_nbr':10}{'exec_pts.':10}{'exm_pts.':10}{'tot_pts.':10}{'grade':10}\n")
	for key, value in students.items():
		if key in exercises and key in exam_scores:
			points = calculate_exercisepoints(exercises[key])
			final_grade = calculate_grade(exam_scores[key], exercises[key])
			total_points = points + exam_scores[key]

			student_info = f"{value:<30}{exercises[key]:<10}{points:<10}{exam_scores[key]:<10}{total_points:<10}{final_grade:<10}"
			file_txt.write(student_info + '\n')

			file_csv.write(f"{key};{value};{final_grade}\n")
