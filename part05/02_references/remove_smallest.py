# Write your solution here

def remove_smallest(numbers: list):

	smallest = min(numbers)
	new_list = []

	for item in numbers:
		if item != smallest:
			new_list.append(item)

	numbers[:] = new_list

