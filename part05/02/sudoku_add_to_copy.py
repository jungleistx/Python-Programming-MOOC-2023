# Write your solution here

def print_sudoku(sudoku: list):

	for i in range(0, 9):
		for j in range(0, 9):
			if sudoku[i][j] != 0:
				print(f"{sudoku[i][j]} ", end="")
			else:
				print(f"_ ", end="")
			if j == 2 or j == 5:
				print(" ", end="")
		print()
		if i == 2 or i == 5:
			print()


def copy_and_add(sudoku: list, row_no: int, column_no: int, number: int):
	new_list = []
	for row in sudoku:
		new_list.append(row[:])

	new_list[row_no][column_no] = number

	return new_list


if __name__ == "__main__":
	s = [
	[ 9, 0, 0, 0, 8, 0, 3, 0, 0 ],
	[ 2, 0, 0, 2, 5, 0, 7, 0, 0 ],
	[ 0, 2, 0, 3, 0, 0, 0, 0, 4 ],
	[ 2, 9, 4, 0, 0, 0, 0, 0, 0 ],
	[ 0, 0, 0, 7, 3, 0, 5, 6, 0 ],
	[ 7, 0, 5, 0, 6, 0, 4, 0, 0 ],
	[ 0, 0, 7, 8, 0, 3, 9, 0, 0 ],
	[ 0, 0, 1, 0, 0, 0, 0, 0, 3 ],
	[ 3, 0, 0, 0, 0, 0, 0, 0, 2 ],
	]

	print_sudoku(s)
	new = copy_and_add(s, 0, 1, 8)
	print("*	*	*	*	*	*	*	*")
	print_sudoku(s)
	print("*	*	*	*	*	*	*	*")
	print_sudoku(new)
