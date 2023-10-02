# Write your solution here

import csv
from datetime import datetime, timedelta

def cheaters() -> list:
	cheater_list = []
	with open('start_times.csv') as start_file, open('submissions.csv') as sub_file:
		start_times = {}
		for line in csv.reader(start_file, delimiter=';'):
			name = line[0]
			time = datetime.strptime(line[1], "%H:%M")
			start_times[name] = time

		for line in csv.reader(sub_file, delimiter=';'):
			name = line[0]
			time = datetime.strptime(line[3], "%H:%M")
			if (time - start_times[name]) > timedelta(hours=3):
				if name not in cheater_list:
					cheater_list.append(name)

	return cheater_list

print(cheaters())