# Write your solution here
# If you use the classes made in the previous exercise, copy them here

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


class AppInterface:
	def __init__(self):
		self.orders = OrderBook()

	def __help(self):
		print('commands:')
		print('0 exit')
		print('1 add order')
		print('2 list finished tasks')
		print('3 list unfinished tasks')
		print('4 mark task as finished')
		print('5 programmers')
		print('6 status of programmer')

	def __add_order(self):
		description = input('description: ')
		input_values = input('programmer and workload estimate: ').split()
		if len(input_values) != 2:
			print('erroneous input')
			return
		programmer, workload = input_values
		try:
			workload = int(workload)
			self.orders.add_order(description, programmer, workload)
			print('added!')
		except:
			print('erroneous input')

	def __list_finished_orders(self):
		fin_tasks = self.orders.finished_orders()
		if fin_tasks:
			for task in fin_tasks:
				print(task)
		else:
			print('no finished tasks')

	def __list_unfinished_orders(self):
		unfin_tasks = self.orders.unfinished_orders()
		if unfin_tasks:
			for task in unfin_tasks:
				print(task)
		else:
			print('no unfinished tasks')

	def __mark_finished(self):
		try:
			id = int(input('id: '))
			self.orders.mark_finished(id)
			print('marked as finished')
		except:
			print('erroneous input')

	def __list_programmers(self):
		for programmer in self.orders.programmers():
			print(programmer)

	def __print_status(self):
		programmer = input('programmer: ')
		try:
			status = self.orders.status_of_programmer(programmer)
			print(f"tasks: finished {status[0]} not finished {status[1]}, hours: done {status[2]} scheduled {status[3]}")
		except:
			print('erroneous input')

	def execute(self):
		self.__help()

		while True:
			print()
			selection = input('command: ')
			if selection == '0':
				return
			elif selection == '1':
				self.__add_order()
			elif selection == '2':
				self.__list_finished_orders()
			elif selection == '3':
				self.__list_unfinished_orders()
			elif selection == '4':
				self.__mark_finished()
			elif selection == '5':
				self.__list_programmers()
			elif selection == '6':
				self.__print_status()

AppInterface().execute()
