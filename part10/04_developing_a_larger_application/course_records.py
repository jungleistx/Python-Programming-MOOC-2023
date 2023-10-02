# # tee ratkaisusi tänne

class Course:
	def __init__(self, name:str, grade:int, credits:int):
		self.__name = name
		self.__grade = grade
		self.__credits = credits

	def update_grade(self, grade:int):
		if grade > self.__grade:
			self.__grade = grade

	def credits(self):
		return self.__credits

	def grade(self):
		return self.__grade

	def __str__(self):
		return f'{self.__name} ({self.__credits} cr) grade {self.__grade}'


class Studies:
	def __init__(self):
		self.__courses = {}

	def _add_course(self):
		name = input('course: ')
		grade = int(input('grade: '))
		credits = int(input('credits: '))
		if name not in self.__courses:
			self.__courses[name] = Course(name, grade, credits)
		else:
			self.__courses[name].update_grade(grade)

	def _get_course_data(self):
		name = input('course: ')
		if name in self.__courses:
			print(self.__courses[name])
		else:
			print('no entry for this course')

	def _statistics(self):
		courses = len(self.__courses)
		tot_credits = self.__get_tot_credits()
		grade = self.__get_tot_grades()
		print(f"{courses} completed courses, a total of {tot_credits} credits")
		print(f"mean {grade/courses:.1f}")
		self.__print_distribution()

	def __print_distribution(self):
		grades = {5: 0, 4: 0, 3: 0, 2: 0, 1: 0}
		for course in self.__courses.values():
			grade = course.grade()
			grades[grade] += 1
		print(f"grade distribution")
		for i in range(5, 0, -1):
			print(f"{i}: {grades[i]*'x'}")

	def __get_tot_grades(self):
		tot_grade = 0
		for course in self.__courses.values():
			tot_grade += course.grade()
		return tot_grade

	def __get_tot_credits(self):
		tot_credits = 0
		for course in self.__courses.values():
			tot_credits += course.credits()
		return tot_credits


class Application:
	def __init__(self):
		self.studies = Studies()

	def help(self):
		print()
		print('1 add course')
		print('2 get course data')
		print('3 statistics')
		print('0 exit')

	def execute(self):
		self.help()
		while True:
			command = input('\ncommand: ')
			if command == '1':
				self.studies._add_course()
			elif command == '2':
				self.studies._get_course_data()
			elif command == '3':
				self.studies._statistics()
			elif command == '0':
				break


Application().execute()
