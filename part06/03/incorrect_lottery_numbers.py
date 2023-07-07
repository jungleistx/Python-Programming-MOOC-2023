# Write your solution here

def filter_incorrect():

	with open('lottery_numbers.csv') as file:
		valid_lines = []
		for line in file:
			parts = line.split(';')
			header = parts[0].split(' ')

			# check week nr == int
			try:
				week_nr = int(header[1])
			except:
				continue

			numbers = parts[1].split(',')

			# check 7 ints
			if len(numbers) != 7:
				continue
			try:
				for number in numbers:
					number = int(number)
			except:
				continue

			# check numbers range 1-39
			valid_nr = True
			for number in numbers:
				number = int(number)
				if number < 1 or number > 39:
					valid_nr = False
					break
			if not valid_nr:
				continue

			# check duplicates
			if len(set(numbers)) != 7:
				continue

			valid_lines.append(line)

	with open ('correct_numbers.csv', 'w') as file:
		for line in valid_lines:
			file.write(line)

# filter_incorrect()