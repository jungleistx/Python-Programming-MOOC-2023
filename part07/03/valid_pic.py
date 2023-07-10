# Write your solution here

from datetime import datetime

def is_it_valid(pic:str) -> bool:
	# check proper length
	if len(pic) != 11:
		return False

	# check that dates are ints
	try:
		day = int(pic[0:2])
		month = int(pic[2:4])
		year = int(pic[4:6])
	except:
		return False

	# check proper century_marker
	century_marker = pic[6]
	century_markers = '+-A'
	if century_marker not in century_markers:
		return False

	# add correct year, based on century_marker
	for i in range(0, 3):
		if century_marker == century_markers[i]:
			year += (18 + i) * 100

	# check invalid dates
	try:
		birthdate = datetime(year, month, day)
	except:
		return False

	# check that identifier is int
	try:
		personal_identifier = int(pic[7:10])
	except:
		return False

	# check that the control character is valid
	identifier = pic[0:6] + pic[7:10]
	identifier = int(identifier)
	index = identifier % 31
	control_characters = '0123456789ABCDEFHJKLMNPRSTUVWXY'
	control_character = pic[-1]

	return control_character == control_characters[index]


# if __name__ == '__main__':
# 	print(is_it_valid('100400A644E'))
# 	print(is_it_valid('230827-906F'))
# 	print(is_it_valid('120488+246L'))
# 	print(is_it_valid('310823A9877'))
# 	print()
# 	print(is_it_valid('230827-906F1'))
# 	print(is_it_valid('290200-1239'))
# 	print(is_it_valid('230857-906F'))
# 	print(is_it_valid('230857+906F'))
# 	print(is_it_valid('120488+246K'))
# 	print(is_it_valid('310823A9878'))

# '''
# valid PICs
# 	230827-906F
# 	120488+246L
# 	310823A9877
# '''
