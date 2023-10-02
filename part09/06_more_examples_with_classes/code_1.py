# Write your solution here:

class Item:
	def __init__(self, name:str, weight:int):
		self.__name = name
		self.__weight = weight

	def name(self):
		return self.__name

	def weight(self):
		return self.__weight

	def __str__(self):
		return f"{self.__name} ({self.__weight} kg)"


class Suitcase:
	def __init__(self, max_weight:int):
		self.__max_weight = max_weight
		self.__items = []

	def add_item(self, item:Item):
		if self.weight() + item.weight() <= self.__max_weight:
			self.__items.append(item)

	def __str__(self):
		size = len(self.__items)
		if size == 1:
			items = 'item'
		else:
			items = 'items'
		return f"{size} {items} ({self.weight()} kg)"

	def print_items(self):
		for item in self.__items:
			print(item)

	def weight(self):
		weight = 0
		for item in self.__items:
			weight += item.weight()
		return weight

	def heaviest_item(self):
		if len(self.__items) == 0:
			return None
		heaviest_size = 0
		heaviest_obj = self.__items[0]
		for item in self.__items:
			if item.weight() > heaviest_obj.weight():
				heaviest_obj = item
				heaviest_size = heaviest_obj.weight()
		return heaviest_obj


class CargoHold:
	def __init__(self, max_weight:int):
		self.__max_weight = max_weight
		self.__suitcases = []

	def add_suitcase(self, suitcase:Suitcase):
		if self.weight() + suitcase.weight() <= self.__max_weight:
			self.__suitcases.append(suitcase)

	def __str__(self):
		size = len(self.__suitcases)
		if size == 1:
			case = 'suitcase'
		else:
			case = 'suitcases'
		return f"{size} {case}, space for {self.__max_weight - self.weight()} kg"

	def print_items(self):
		for item in self.__suitcases:
			item.print_items()

	def weight(self):
		weight = 0
		for suitcase in self.__suitcases:
			weight += suitcase.weight()
		return weight


if __name__ == "__main__":
	book = Item("ABC Book", 2)
	phone = Item("Nokia 3210", 1)
	print("Name of the book:", book.name())
	print("Weight of the book:", book.weight())
	print("Book:", book)
	print("Phone:", phone)
	print()

	book = Item("ABC Book", 2)
	phone = Item("Nokia 3210", 1)
	brick = Item("Brick", 4)
	suitcase = Suitcase(5)
	print(suitcase)
	suitcase.add_item(book)
	print(suitcase)
	suitcase.add_item(phone)
	print(suitcase)
	suitcase.add_item(brick)
	print(suitcase)
	print()

	book = Item("ABC Book", 2)
	phone = Item("Nokia 3210", 1)
	brick = Item("Brick", 4)
	suitcase = Suitcase(10)
	suitcase.add_item(book)
	suitcase.add_item(phone)
	suitcase.add_item(brick)
	print("The suitcase contains the following items:")
	suitcase.print_items()
	combined_weight = suitcase.weight()
	print(f"Combined weight: {combined_weight} kg")
	print()

	book = Item("ABC Book", 2)
	phone = Item("Nokia 3210", 1)
	brick = Item("Brick", 4)
	suitcase = Suitcase(10)
	suitcase.add_item(book)
	suitcase.add_item(phone)
	suitcase.add_item(brick)
	heaviest = suitcase.heaviest_item()
	print(f"The heaviest item: {heaviest}")
	print()

	cargo_hold = CargoHold(1000)
	print(cargo_hold)
	book = Item("ABC Book", 2)
	phone = Item("Nokia 3210", 1)
	brick = Item("Brick", 4)
	adas_suitcase = Suitcase(10)
	adas_suitcase.add_item(book)
	adas_suitcase.add_item(phone)
	peters_suitcase = Suitcase(10)
	peters_suitcase.add_item(brick)
	cargo_hold.add_suitcase(adas_suitcase)
	print(cargo_hold)
	cargo_hold.add_suitcase(peters_suitcase)
	print(cargo_hold)
	print()

	book = Item("ABC Book", 2)
	phone = Item("Nokia 3210", 1)
	brick = Item("Brick", 4)
	adas_suitcase = Suitcase(10)
	adas_suitcase.add_item(book)
	adas_suitcase.add_item(phone)
	peters_suitcase = Suitcase(10)
	peters_suitcase.add_item(brick)
	cargo_hold = CargoHold(1000)
	cargo_hold.add_suitcase(adas_suitcase)
	cargo_hold.add_suitcase(peters_suitcase)
	print("The suitcases in the cargo hold contain the following items:")
	cargo_hold.print_items()
	print()