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