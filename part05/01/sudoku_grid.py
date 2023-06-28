# Write your solution here

def block_correct(sudoku: list, row_no: int, column_no: int) -> bool:

	numbers = []
	for i in range(row_no, row_no + 3):
		for j in range(column_no, column_no + 3):
			numbers.append(sudoku[i][j])

	for i in range(1, 10):
		if numbers.count(i) > 1:
			return False

	return True


def column_correct(sudoku: list, column_no: int) -> bool:

	numbers = []

	for row in sudoku:
		numbers.append(row[column_no])

	for i in range(1, 10):
		if numbers.count(i) > 1:
			return False

	return True


def row_correct(sudoku: list, row_no: int) -> bool:
	row = sudoku[row_no]

	for i in range(1, 10):
		if row.count(i) > 1:
			return False

	return True


def sudoku_grid_correct(sudoku: list) -> bool:

	for i in range(0, 9):
		for j in range(0, 9):
			if j == 0:
				if row_correct(sudoku, i) == False:
					return False
			if i % 3 == 0 and j % 3 == 0 and i < 9 and j < 9:
				if block_correct(sudoku, i, j) == False:
					return False
			if column_correct(sudoku, j) == False:
				return False

	return True
