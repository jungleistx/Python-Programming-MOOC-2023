# Write your solution here

def transpose(matrix: list):

	new_matrix = []
	for i in range(len(matrix)):
		row = []
		for j in range(len(matrix)):
			row.append(matrix[j][i])

		new_matrix.append(row)
	matrix[:] = new_matrix
