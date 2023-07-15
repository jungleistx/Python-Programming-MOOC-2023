# WRITE YOUR SOLUTION HERE:

class Car:
	def __init__(self):
		self.__tank = 0
		self.__mileage = 0

	def fill_up(self):
		self.__tank = 60

	def drive(self, km:int):
		if km >= self.__tank:
			km = self.__tank

		self.__mileage += km
		self.__tank -= km

	def __str__(self):
		return f"Car: odometer reading: {self.__mileage} km, petrol remaining {self.__tank} litres"

if __name__ == "__main__":
	car = Car()
	print(car)
	car.fill_up()
	print(car)
	car.drive(20)
	print(car)
	car.drive(50)
	print(car)
	car.drive(10)
	print(car)
	car.fill_up()
	car.fill_up()
	print(car)