# Write your solution here

def double_items(numbers: list):

	new_list = []
	for i in range(len(numbers)):
		new_list.append(numbers[i] * 2)

	return new_list