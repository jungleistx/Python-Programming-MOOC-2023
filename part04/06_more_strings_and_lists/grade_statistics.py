# Write your solution here
def main():
	calculate_grades()


def print_grades(grades: list, total_points: int, num_of_grades: int):
	print("Statistics:")
	print(f"Points average: {total_points / num_of_grades:.1f}")

	fails = grades.count(0)
	print(f"Pass percentage: {(num_of_grades - fails) / num_of_grades * 100:.1f}")
	print("Grade distribution:")

	grade_counter = 5
	while grade_counter >= 0:
		amount = grades.count(grade_counter)
		print(f"  {grade_counter}: {amount * '*'}")
		grade_counter -= 1


def get_grade(score: int, exam_points: int) -> int:
	if exam_points < 10:
		grade = 0
	else:
		if score <= 14:
			grade = 0
		elif score <= 17:
			grade = 1
		elif score <= 20:
			grade = 2
		elif score <= 23:
			grade = 3
		elif score <= 27:
			grade = 4
		else:
			grade = 5
	return grade


def calculate_grades():
	grades = []
	num_of_grades = 0
	total_points = 0

	while True:
		user_input = input("Exam points and exercises completed: ")
		if len(user_input) == 0:
			break

		space = user_input.find(" ")
		exam_points = int(user_input[:space])
		exercises = int(user_input[space + 1:])

		score = 0
		score = exam_points
		score += int(exercises * 0.1)

		grade = get_grade(score, exam_points)
		grades.append(grade)
		num_of_grades += 1
		total_points += score
	print_grades(grades, total_points, num_of_grades)


main()
