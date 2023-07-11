# Write your solution here

import csv
from datetime import datetime, timedelta

def final_points() -> dict:
	# save starting times to a dict
	student_points = {}
	with open('start_times.csv') as start_file, open('submissions.csv') as sub_file:
		start_times = {}
		for line in csv.reader(start_file, delimiter=';'):
			name = line[0]
			time = datetime.strptime(line[1], '%H:%M')
			start_times[name] = time

		# save submission times to a dict
		sub_times = {}
		for line in csv.reader(sub_file, delimiter=';'):
			name = line[0]
			time = datetime.strptime(line[3], '%H:%M')
			task = line[1]
			points = line[2]
			# save only submissions with less than 3 hours
			if (time - start_times[name]) <= timedelta(hours=3):
				if name not in sub_times:
					sub_times[name] = {}
				# save best score
				if task not in sub_times[name]:
					sub_times[name][task] = points
				elif sub_times[name][task] < points:
					sub_times[name][task] = points

	# count total points from courses
	for name, values in sub_times.items():
		tot_points = 0
		for course_nr, value in values.items():
			tot_points += int(value)
		student_points[name] = tot_points

	return student_points

# print(final_points())