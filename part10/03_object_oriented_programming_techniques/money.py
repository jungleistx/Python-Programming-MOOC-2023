# TEE RATKAISUSI TÄHÄN:
class Money:
	def __init__(self, euros: int, cents: int):
		self.__euros = euros
		self.__cents = cents

	def __str__(self):
		return f"{self.__euros}.{self.__cents:02} eur"

	# to avoid rounding errors with small numbers, multiply euros with 100
	def __get_value(self):
		return self.__euros * 100 + self.__cents

	def __set_value(self, money:float):
		euros = money // 100
		self.__euros = euros
		self.__cents = money - euros * 100

	def __eq__(self, another:'Money'):
		return self.__get_value() == another.__get_value()

	def __lt__(self, another:'Money'):
		return self.__get_value() < another.__get_value()

	def __gt__(self, another:'Money'):
		return self.__get_value() > another.__get_value()

	def __ne__(self, another:'Money'):
		return self.__get_value() != another.__get_value()

	def __add__(self, another:'Money'):
		new_money = Money(0, 0)
		new_money.__set_value(self.__get_value() + another.__get_value())
		return new_money

	def __sub__(self, another:'Money'):
		if self.__get_value() - another.__get_value() < 0:
			raise ValueError('a negative result is not allowed')
		new_money = Money(0, 0)
		new_money.__set_value(self.__get_value() - another.__get_value())
		return new_money


if __name__ == "__main__":

	e1 = Money(4, 10)
	e2 = Money(2, 5)
	e3 = Money(4, 10)
	print(e1)
	print(e2)
	print(e3)
	print(e1 == e2)
	print(e1 == e3)
	print()

	e1 = Money(4, 10)
	e2 = Money(2, 5)
	print(e1 != e2)
	print(e1 < e2)
	print(e1 > e2)
	print()

	e1 = Money(4, 5)
	e2 = Money(2, 95)
	e3 = e1 + e2
	e4 = e1 - e2
	print(e3)
	print(e4)
	# e5 = e2-e1
	print()

	print(e1)
	e1.euros = 1000
	print(e1)
	print()