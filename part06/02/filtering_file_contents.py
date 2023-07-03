# Write your solution here

def check_answer(problem:str, given_answer:str) -> bool:
	i = 0
	while problem[i].isdigit():
		i += 1

	num1 = problem[:i]
	num1 = int(num1)
	operator = problem[i]
	num2 = problem[i + 1:]
	num2 = int(num2)

	if operator == '+':
		answer = num1 + num2
	elif operator == '-':
		answer = num1 - num2

	if answer == int(given_answer):
		return True
	else:
		return False


def filter_solutions():

	incorrect = []
	correct = []
	with open('solutions.csv') as file:

		for line in file:
			elements = line.split(';')
			if check_answer(elements[1], elements[2]):
				correct.append(line)
			else:
				incorrect.append(line)

	with open('correct.csv', 'w') as file:
		for row in correct:
			file.write(row)

	with open('incorrect.csv', 'w') as file:
		for row in incorrect:
			file.write(row)


# filter_solutions()