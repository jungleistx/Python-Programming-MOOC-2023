# Write your solution here

from datetime import datetime, timedelta

try:
	birthday = int(input('Day: '))
	birthmonth = int(input('Month: '))
	birthyear = int(input('Year: '))
except:
	raise ValueError('Invalid input')

real_birthday = datetime(birthyear, birthmonth, birthday)
millenium = datetime(2000, 1, 1)
if millenium <= real_birthday:
	print('You weren\'t born yet on the eve of the new millennium.')
else:
	difference = millenium - real_birthday - timedelta(days=1)
	print(f'You were {difference.days} days old on the eve of the new millennium.')