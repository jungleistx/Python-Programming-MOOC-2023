# Write your solution here:

class Person:
	def __init__(self, name:str):
		self.name = name

	def return_first_name(self) -> str:
		if self.is_fullname(self.name):
			names = self.name.split(' ')
			return names[0]
		else:
			return self.name

	def return_last_name(self) -> str:
		if self.is_fullname(self.name):
			names = self.name.split(' ')
			return names[-1]
		else:
			return self.name

	def is_fullname(self, name:str) -> bool:
		if name.count(' ') > 0:
			return True
		return False
