# Write your solution here

from datetime import datetime, timedelta

# get input
filename = input('Filename: ')
start_date = input('Starting date: ')
try:
	days = int(input('How many days: '))
except:
	raise ValueError("Invalid input")
print('Please type in screen time in minutes on each day (TV computer mobile):')

# convert input to date-format
start_date = datetime.strptime(start_date, "%d.%m.%Y")

total_minutes = 0
screen_times = {}

# get user input
for i in range(days):
	current_date = start_date + timedelta(days=i)
	current_date_formatted = datetime.strftime(current_date, '%d.%m.%Y')

	todays_times = input(f'Screen time {current_date_formatted}: ').split(' ')
	todays_time_values = list(map(int, todays_times))
	total_minutes += sum(todays_time_values)

	# add to dict
	minutes = f'{todays_times[0]}/{todays_times[1]}/{todays_times[2]}'
	screen_times[current_date_formatted] = minutes

with open(filename, 'w') as file:
	end_date = start_date + timedelta(days=(days-1))
	end_date_formatted = end_date.strftime("%d.%m.%Y")
	start_date_formatted = start_date.strftime("%d.%m.%Y")
	file.write(f'Time period: {start_date_formatted}-{end_date_formatted}\n')
	file.write(f'Total minutes: {total_minutes}\n')
	file.write(f'Average minutes: {total_minutes/days:.1f}\n')

	# write to file from dict
	for date, minutes in screen_times.items():
		file.write(f'{date}: {minutes}\n')

print(f'Data stored in {filename}')
