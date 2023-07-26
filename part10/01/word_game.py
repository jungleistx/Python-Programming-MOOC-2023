# Write your solution here
import random

class WordGame():
	def __init__(self, rounds: int):
		self.wins1 = 0
		self.wins2 = 0
		self.rounds = rounds

	def round_winner(self, player1_word: str, player2_word: str):
		# determine a random winner
		return random.randint(1, 2)

	def play(self):
		print("Word game:")
		for i in range(1, self.rounds+1):
			print(f"round {i}")
			answer1 = input("player1: ")
			answer2 = input("player2: ")

			if self.round_winner(answer1, answer2) == 1:
				self.wins1 += 1
				print("player 1 won")
			elif self.round_winner(answer1, answer2) == 2:
				self.wins2 += 1
				print("player 2 won")
			else:
				pass # it's a tie

		print("game over, wins:")
		print(f"player 1: {self.wins1}")
		print(f"player 2: {self.wins2}")


class LongestWord(WordGame):
	def __init__(self, rounds: int):
		super().__init__(rounds)

	def round_winner(self, player1_word: str, player2_word: str):
		# your code for determining the winner goes here
		len_p1 = len(player1_word)
		len_p2 = len(player2_word)
		if len_p1 > len_p2:
			return 1
		elif len_p1 < len_p2:
			return 2
		else:
			return 0


class MostVowels(WordGame):
	def __init__(self, rounds: int):
		super().__init__(rounds)

	def count_vowels(self, word:str) -> int:
		vowels = 'aeiouy'
		tot_vowels = 0
		for letter in word:
			if letter in vowels:
				tot_vowels += 1
		return tot_vowels

	def round_winner(self, player1_word: str, player2_word: str):
		vowels_p1 = self.count_vowels(player1_word)
		vowels_p2 = self.count_vowels(player2_word)
		if vowels_p1 > vowels_p2:
			return 1
		elif vowels_p1 < vowels_p2:
			return 2
		else:
			return 0


class RockPaperScissors(WordGame):
	def __init__(self, rounds: int):
		super().__init__(rounds)

	def round_winner(self, player1_word: str, player2_word: str):
		valid_options = ['rock', 'paper', 'scissors']
		valid_p1 = player1_word in valid_options
		valid_p2 = player2_word in valid_options

		# atleast one input is invalid
		if valid_p1 and not valid_p2:
			return 1
		elif not valid_p1 and valid_p2:
			return 2
		elif not valid_p1 and not valid_p2:
			return 0

		# tie
		if player1_word == player2_word:
			return 0

		# remaining options
		if player1_word == 'rock':
			if player2_word == 'scissors':
				return 1
			else:
				return 2
		elif player1_word == 'paper':
			if player2_word == 'rock':
				return 1
			else:
				return 2
		else:
			if player2_word == 'paper':
				return 1
			else:
				return 2


if __name__ == "__main__":

	# p = WordGame(3)
	# p.play()

	# p = LongestWord(3)
	# p.play()

	# p = MostVowels(3)
	# p.play()

	p = RockPaperScissors(4)
	p.play()