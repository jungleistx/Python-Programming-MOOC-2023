# WRITE YOUR SOLUTION HERE:

class SimpleDate:
	def __init__(self, day:int, month:int, year:int):
		self._day = day
		self._month = month
		self._year = year

	def __str__(self):
		return f"{self._day}.{self._month}.{self._year}"

	def __get_days(self):
		return self._day + self._month * 30 + self._year * 30 * 12

	def __lt__(self, other:'SimpleDate'):
		return self.__get_days() < other.__get_days()

	def __gt__(self, other:'SimpleDate'):
		return self.__get_days() > other.__get_days()

	def __eq__(self, other:'SimpleDate'):
		return self.__get_days() == other.__get_days()

	def __ne__(self, other:'SimpleDate'):
		return self.__get_days() != other.__get_days()

	def __add__(self, days_added:int):
		days = self.__get_days() + days_added
		years = days // (30 * 12)
		days -= (years * 30 * 12)
		months = days // 30
		days -= (months * 30)
		return SimpleDate(days, months, years)

	def __sub__(self, other:'SimpleDate'):
		return abs(self.__get_days() - other.__get_days())


if __name__ == "__main__":
	d1 = SimpleDate(4, 10, 2020)
	d2 = SimpleDate(28, 12, 1985)
	d3 = SimpleDate(28, 12, 1985)
	print(d1)
	print(d2)
	print(d1 == d2)
	print(d1 != d2)
	print(d1 == d3)
	print(d1 < d2)
	print(d1 > d2)

	d1 = SimpleDate(4, 10, 2020)
	d2 = SimpleDate(28, 12, 1985)
	d3 = d1 + 3
	d4 = d2 + 400
	print(d1)
	print(d2)
	print(d3)
	print(d4)

	d1 = SimpleDate(4, 10, 2020)
	d2 = SimpleDate(2, 11, 2020)
	d3 = SimpleDate(28, 12, 1985)
	print(d2-d1)
	print(d1-d2)
	print(d1-d3)