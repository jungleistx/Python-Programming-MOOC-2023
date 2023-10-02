# WRITE YOUR SOLUTION HERE:
class Person:
	def __init__(self, name: str, height: int):
		self.name = name
		self.height = height

	def __str__(self):
		return self.name

class Room:
	def __init__(self):
		self.persons = []

	def add(self, person:Person):
		self.persons.append(person)

	def is_empty(self) -> bool:
		if not self.persons:
			return True
		return False

	def print_contents(self):
		size = len(self.persons)
		tot_height = 0
		for person in self.persons:
			tot_height += person.height
		print(f"There are {size} persons in the room, and their combined height is {tot_height} cm")
		for person in self.persons:
			print(f"{person.name} ({person.height} cm)")

	def shortest(self) -> Person:
		if not self.persons:
			return None
		shortest = self.persons[0]
		for person in self.persons:
			if person.height < shortest.height:
				shortest = person
		return shortest

	def remove_shortest(self) -> Person:
		if not self.persons:
			return None
		shortest = self.shortest()
		self.persons.remove(shortest)
		return shortest


if __name__ == "__main__":
	room = Room()
	print("Is the room empty?", room.is_empty())
	room.add(Person("Lea", 183))
	room.add(Person("Kenya", 172))
	room.add(Person("Ally", 166))
	room.add(Person("Nina", 162))
	room.add(Person("Dorothy", 155))
	print("Is the room empty?", room.is_empty())
	room.print_contents()

	print()
	room = Room()
	print("Is the room empty?", room.is_empty())
	print("Shortest:", room.shortest())
	room.add(Person("Lea", 183))
	room.add(Person("Kenya", 172))
	room.add(Person("Nina", 162))
	room.add(Person("Ally", 166))
	print()
	print("Is the room empty?", room.is_empty())
	print("Shortest:", room.shortest())
	print()
	room.print_contents()

	print()
	room = Room()
	room.add(Person("Lea", 183))
	room.add(Person("Kenya", 172))
	room.add(Person("Nina", 162))
	room.add(Person("Ally", 166))
	room.print_contents()
	print()
	removed = room.remove_shortest()
	print(f"Removed from room: {removed.name}")
	print()
	room.print_contents()