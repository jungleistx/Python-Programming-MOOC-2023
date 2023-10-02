# Write your solution here

def get_average(person:dict) -> float:
	average = (person['result1'] + person['result2'] + person['result3']) / 3
	return average

def smallest_average(person1:dict, person2:dict, person3:dict) -> dict:
	smallest = person1
	if get_average(person2) < get_average(smallest):
		smallest = person2
	if get_average(person3) < get_average(smallest):
		smallest = person3

	return smallest


# person1 = {"name": "Mary", "result1": 2, "result2": 3, "result3": 3}
# person3 = {"name": "Larry", "result1": 3, "result2": 1, "result3": 1}
# person2 = {"name": "Gary", "result1": 5, "result2": 1, "result3": 8}

# print(smallest_average(person1, person2, person3))
# print()
