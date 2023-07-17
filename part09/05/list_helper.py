# WRITE YOUR SOLUTION HERE:

class ListHelper:

	@classmethod
	def greatest_frequency(cls, my_list:list):
		most_hits = 0
		most_hits_nr = 0
		for number in my_list:
			if my_list.count(number) > most_hits:
				most_hits = my_list.count(number)
				most_hits_nr = number
		return most_hits_nr

	@classmethod
	def doubles(cls, my_list:list):
		doubles_list = []
		for number in my_list:
			if my_list.count(number) > 1:
				if number not in doubles_list:
					doubles_list.append(number)
		return len(doubles_list)
