# Write your solution here

def new_person(name:str, age:int) -> tuple:

	if len(name) < 1 or age > 150 or name.count(' ') < 1 or len(name) > 40 or age < 0:
		raise ValueError()

	return (name, age)