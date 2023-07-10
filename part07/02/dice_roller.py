# Write your solution here

from random import choice

def get_die_values(die:str) -> list:
	if die == 'A':
		return [3, 3, 3, 3, 3, 6]
	elif die == 'B':
		return [2, 2, 2, 5, 5, 5]
	elif die == 'C':
		return [1, 4, 4, 4, 4, 4]
	else:
		return [0, 0, 0, 0, 0, 0]


def roll(die:str) -> int:
	values = get_die_values(die)
	return choice(values)


def play(die1:str, die2:str, times:int) -> tuple:
	die1_wins = 0
	die2_wins = 0
	ties = 0

	for i in range(times):
		result1 = roll(die1)
		result2 = roll(die2)
		if result1 > result2:
			die1_wins += 1
		elif result1 < result2:
			die2_wins += 1
		else:
			ties += 1

	return (die1_wins, die2_wins, ties)


if __name__ == '__main__':
	for i in range(20):
		print(roll("A"), " ", end="")
	print()
	for i in range(20):
		print(roll("B"), " ", end="")
	print()
	for i in range(20):
		print(roll("C"), " ", end="")
	print()

	result = play("A", "C", 1000)
	print(result)
	result = play("B", "B", 1000)
	print(result)