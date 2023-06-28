# write your solution here

def matrix_sum() -> int:
	with open("matrix.txt") as file:
		sum_total = 0
		for line in file:
			values = line.split(',')
			for i in range(len(values)):
				values[i] = int(values[i])
			sum_total += sum(values)
	return sum_total


def matrix_max() -> int:
	current_max = 0
	with open("matrix.txt") as file:
		for line in file:
			values = line.split(",")
			if int(max(values)) > current_max:
				current_max = int(max(values))
	return current_max


def row_sums() -> int:
	sum_list = []
	with open("matrix.txt") as file:
		for line in file:
			values = line.split(',')
			for i in range(len(values)):
				values[i] = int(values[i])
			sum_list.append(sum(values))
	return sum_list
