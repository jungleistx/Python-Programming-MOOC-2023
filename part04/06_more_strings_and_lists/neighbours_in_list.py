# Write your solution here

def longest_series_of_neighbours(num_list: list) -> int:

	current_len = 1
	longest = 1
	last_number = num_list[0]

	for i in range(1, len(num_list)):

		if abs(last_number - num_list[i]) <= 1:
			current_len += 1
		else:
			current_len = 1

		if current_len > longest:
			longest = current_len

		last_number = num_list[i]

	return longest

if __name__ == "__main__":
	my_list = [1, 2, 5, 7, 6, 5, 6, 3, 4, 1, 0]
	print("\n", longest_series_of_neighbours(my_list))
