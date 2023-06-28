# Write your solution here

def even_numbers(num_list : list) -> list:

	new_list = []

	for num in num_list:
		if num % 2 == 0:
			new_list.append(num)

	return new_list