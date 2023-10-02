# Write your solution here

def row_correct(sudoku: list, row_no: int) -> bool:
	row = sudoku[row_no]

	for i in range(1, 10):
		if row.count(i) > 1:
			return False

	return True