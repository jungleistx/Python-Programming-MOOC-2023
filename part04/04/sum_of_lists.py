# Write your solution here

def list_sum(list1 : list, list2 : list) -> list:

	new_list = []

	for i in range(len(list1)):
		new_list.append(list1[i] + list2[i])

	return new_list