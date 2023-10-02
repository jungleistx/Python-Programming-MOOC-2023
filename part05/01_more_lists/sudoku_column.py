# Write your solution here

def column_correct(sudoku: list, column_no: int) -> bool:

	numbers = []

	for row in sudoku:
		numbers.append(row[column_no])

	for i in range(1, 10):
		if numbers.count(i) > 1:
			return False

	return True
