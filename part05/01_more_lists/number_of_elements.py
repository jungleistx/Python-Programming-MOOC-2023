# Write your solution here

def count_matching_elements(my_matrix: list, element: int) -> int:

	hits = 0
	for i in range(len(my_matrix)):
		for j in range(len(my_matrix[i])):
			if my_matrix[i][j] == element:
				hits += 1

	return hits


if __name__ == "__main__":
	print(count_matching_elements([[1,2,3], [1,4,5,6], [7,8,9,12,1]], 1))
