# Write your solution here

def sum_of_positives(num_list : list) -> int:

	positives = 0

	for num in num_list:
		if num > 0:
			positives += num

	return positives