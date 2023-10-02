# Write your solution here

def add_student(database: dict, student: str):
	if student not in database:
		database[student] = []


def print_student(database: dict, student: str):
	if student in database:
		print(f"{student}:")
		if len(database[student]) == 0:
			print(" no completed courses")
		else:
			courses_finished = 0
			for course in database[student]:
				if course[1] > 0:
					courses_finished += 1

			print(f" {courses_finished} completed courses:")

			average = 0.0
			for course in database[student]:
				if course[1] > 0:
					print(f"  {course[0]} {course[1]}")
					average += course[1]

			print(f" average grade {(average / courses_finished):.1f}")

	else:
		print(f"{student}: no such person in the database")


def add_course(database: dict, student: str, new_course: tuple):
	if student in database:
		if new_course[1] > 0:	# grade is over 0
			if len(database[student]) == 0:
				database[student].append(new_course)
			else:
				found = False
				for course in database[student]:
					if course[0] == new_course[0]:	# course is already taken
						if new_course[1] > course[1]:
							database[student].remove(course)
							database[student].append(new_course)
						found = True
				if not found:
					database[student].append(new_course)


def summary(database: dict):
	students = len(database)

	most_courses = 0
	most_courses_name = ""
	best_average = 0.0
	best_average_name = ""

	for student in database:
		if len(database[student]) > most_courses:
			most_courses = len(database[student])
			most_courses_name = student

		average = 0.0
		for course in database[student]:
			average += course[1]

		if best_average < average / len(database[student]):
			best_average = average / len(database[student])
			best_average_name = student

	print(f"students {students}")
	print(f"most courses completed {most_courses} {most_courses_name}")
	print(f"best average grade {best_average:.1f} {best_average_name}")
