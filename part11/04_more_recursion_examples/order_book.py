# Write your solution here:

class Task:
	id = 1

	def __init__(self, description:str, programmer:str, workload:int):
		self.description = description
		self.programmer = programmer
		self.workload = workload
		self.finished = False
		self.id = Task.id
		Task.id += 1

	def __str__(self):
		finish = "FINISHED" if self.finished else "NOT FINISHED"
		return f"{self.id}: {self.description} ({self.workload} hours), programmer {self.programmer} {finish}"

	def is_finished(self):
		return self.finished

	def mark_finished(self):
		self.finished = True


class OrderBook:
	def __init__(self):
		self._orders = []

	def add_order(self, description, programmer, workload):
		self._orders.append(Task(description, programmer, workload))

	def all_orders(self):
		return self._orders

	def programmers(self):
		return list(set([task.programmer for task in self._orders]))

	def mark_finished(self, id: int):
		for task in self._orders:
			if task.id == id:
				task.mark_finished()
				return
		raise ValueError(f'Id ({id}) not found')

	def finished_orders(self):
		return [task for task in self._orders if task.is_finished()]

	def unfinished_orders(self):
		return [task for task in self._orders if not task.is_finished()]

	def status_of_programmer(self, programmer: str):
		if programmer not in self.programmers():
			raise ValueError(f'Programmer \'{programmer}\' not found')

		fin_tasks = [task for task in self._orders if task.programmer == programmer and task.is_finished()]
		unfin_tasks = [task for task in self._orders if task.programmer == programmer and not task.is_finished()]
		fin_hours = sum(task.workload for task in fin_tasks)
		unfin_hours = sum(task.workload for task in unfin_tasks)

		return (len(fin_tasks), len(unfin_tasks), fin_hours, unfin_hours)


if __name__ == "__main__":
	# t1 = Task("program hello world", "Eric", 3)
	# print(t1.id, t1.description, t1.programmer, t1.workload)
	# print(t1)
	# print(t1.is_finished())
	# t1.mark_finished()
	# print(t1)
	# print(t1.is_finished())
	# t2 = Task("program webstore", "Adele", 10)
	# t3 = Task("program mobile app for workload accounting", "Eric", 25)
	# print(t2)
	# print(t3)

	# print()
	# orders = OrderBook()
	# orders.add_order("program webstore", "Adele", 10)
	# orders.add_order("program mobile app for workload accounting", "Eric", 25)
	# orders.add_order("program app for practising mathematics", "Adele", 100)
	# for order in orders.all_orders():
	# 	print(order)
	# print()
	# for programmer in orders.programmers():
	# 	print(programmer)

	# print()
	# orders = OrderBook()
	# orders.add_order("program webstore", "Adele", 10)
	# orders.add_order("program mobile app for workload accounting", "Eric", 25)
	# orders.add_order("program app for practising mathematics", "Adele", 100)
	# orders.mark_finished(1)
	# orders.mark_finished(2)
	# for order in orders.all_orders():
	# 	print(order)

	orders = OrderBook()
	orders.add_order("program webstore", "Adele", 10)
	orders.add_order("program mobile app for workload accounting", "Adele", 25)
	orders.add_order("program app for practising mathematics", "Adele", 100)
	orders.add_order("program the next facebook", "Eric", 1000)
	orders.mark_finished(1)
	orders.mark_finished(2)
	status = orders.status_of_programmer("Adele")
	print(status)