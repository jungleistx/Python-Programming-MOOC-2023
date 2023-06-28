# Write your solution here

def oldest_person(people: list):

	year = people[0][1]
	name = people[0][0]
	for person in people:
		if person[1] < year:
			name = person[0]
			year = person[1]
	return name
