# write your solution here

def largest() -> int:
	with open("numbers.txt") as textfile:

		largest = 0

		for line in textfile:
			if int(line) > largest:
				largest = int(line)

	return largest
