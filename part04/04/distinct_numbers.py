# Write your solution here

def distinct_numbers(num_list : list) -> list:

	new_list = []

	for num in num_list:
		if num not in new_list:
			new_list.append(num)

	new_list.sort()

	return new_list