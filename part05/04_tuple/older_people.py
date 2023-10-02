# Write your solution here

def older_people(people: list, year: int) -> list:
	new_list = []

	for person in people:
		if person[1] < year:
			new_list.append(person[0])

	return new_list
