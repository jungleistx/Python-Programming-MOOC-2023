# Write your solution here:

class Clock:
	def __init__(self, hour:int, minute:int, second:int):
		self.hour = hour
		self.minute = minute
		self.second = second

	def tick(self):
		if self.second < 59:
			self.second += 1
		else:
			self.second = 0
			if self.minute < 59:
				self.minute += 1
			else:
				self.minute = 0
				if self.hour < 23:
					self.hour += 1
				else:
					self.hour = 0

	def set(self, hour:int, minute:int):
		self.hour = hour
		self.minute = minute
		self.second = 0

	def __str__(self):
		return f"{self.hour:02}:{self.minute:02}:{self.second:02}"