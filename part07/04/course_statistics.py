# Write your solution here

import urllib.request
import json

def main():
	for course in retrieve_all():
		print(course)
	for data, value in retrieve_course('docker2019').items():
		print(f'{data}: {value}')


def retrieve_all() -> list:
	courselist = []

	request = urllib.request.urlopen('https://studies.cs.helsinki.fi/stats-mock/api/courses')
	data = json.loads(request.read())

	for course in data:
		if course['enabled'] == True:
			fullname = course['fullName']
			name = course['name']
			year = course['year']
			sum_exercises = sum(course['exercises'])
			courselist.append((fullname, name, year, sum_exercises))

	return courselist
# {
# 	'week': 0,
# 	'exercises': [6, 14, 20, 22, 22, 22, 21, 21, 26, 27],
# 	'enabled': True,
# 	'miniproject': False,
# 	'peerReviewOpen': False,
# 	'extension': True,
# 	'_id': '5c7f97d3b7e42b00495261de',
# 	'year': 2020,
# 	'term': 'Year',
# 	'fullName': 'Full Stack Open 2020',
# 	'name': 'ofs2019',
# 	'url': 'https://fullstackopen.com/',
# 	'__v': 16
# }


def retrieve_course(course_name:str) -> dict:
	course_stats = {}
	url = 'https://studies.cs.helsinki.fi/stats-mock/api/courses/' + course_name + '/stats'
	request = urllib.request.urlopen(url)
	data = json.loads(request.read())

	tot_hours = 0
	max_students = 0
	tot_exercises = 0
	for week_nr, week_data in data.items():
		if week_data['students'] > max_students:
			max_students = week_data['students']
		tot_hours += week_data['hour_total']
		tot_exercises += week_data['exercise_total']

	course_stats['weeks'] = len(data)
	course_stats['students'] = max_students
	course_stats['hours'] = tot_hours
	course_stats['hours_average'] = tot_hours // max_students
	course_stats['exercises'] = tot_exercises
	course_stats['exercises_average'] = tot_exercises // max_students
	return course_stats
# {'0':
		# {'students': 220,
		# 'hour_total': 286,
		# 'exercise_total': 218,
		# 'hours': [None, 176, 11, 3, 1, 1, None, None, 6]},
#  '1':
		# {'students': 176,
		# 'hour_total': 2421,
		# 'exercise_total': 2748,
		# 'hours': [None, 6, 3, 3, 4, 9, 5, 8, 13, 4, 28, 1, 14, 2, 3, 20, 2, 4, 3, None, 15, 1, 1, None, 6, 5, None, 1, 2, None, 8, None, None, None, None, 1, None, None, None, None, 2, 2]}}

main()