from functools import reduce

class CourseAttempt:
	def __init__(self, course_name: str, grade: int, credits: int):
		self.course_name = course_name
		self.grade = grade
		self.credits = credits

	def __str__(self):
		return f"{self.course_name} ({self.credits} cr) grade {self.grade}"

# Write your solution

def sum_of_all_credits(attempts:list):
	return reduce(lambda x, item: x + item.credits, attempts, 0)


def sum_of_passed_credits(attempts:list):
	passed = filter(lambda x: x.grade > 0, attempts)
	return reduce(lambda x, item: x + item.credits, passed, 0)


def average(attempts:list):
	passed = list(filter(lambda x: x.grade > 0, attempts))
	return (reduce(lambda x, item: x + item.grade, passed, 0) / len(passed))


if __name__ == "__main__":
	s1 = CourseAttempt("Introduction to Programming", 5, 5)
	s2 = CourseAttempt("Advanced Course in Programming", 4, 5)
	s3 = CourseAttempt("Data Structures and Algorithms", 3, 10)
	credit_sum = sum_of_all_credits([s1, s2, s3])
	print(credit_sum)

	s1 = CourseAttempt("Introduction to Programming", 5, 5)
	s2 = CourseAttempt("Advanced Course in Programming", 0, 4)
	s3 = CourseAttempt("Data Structures and Algorithms", 3, 10)
	credit_sum = sum_of_passed_credits([s1, s2, s3])
	print(credit_sum)

	s1 = CourseAttempt("Introduction to Programming", 5, 5)
	s2 = CourseAttempt("Advanced Course in Programming", 0, 4)
	s3 = CourseAttempt("Data Structures and Algorithms", 3, 10)
	ag = average([s1, s2, s3])
	print(ag)