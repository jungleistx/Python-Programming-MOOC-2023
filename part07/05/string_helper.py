# Write your solution here

from string import ascii_letters, digits

def change_case(orig_string:str) -> str:
	new_str = ''
	for character in orig_string:
		if character.islower():
			new_str += character.upper()
		elif character.isupper():
			new_str += character.lower()
		else:
			new_str += character
	return new_str


def split_in_half(orig_string:str) -> tuple:
	first_half = ''
	last_half = ''
	half_point = len(orig_string) // 2
	first_half = orig_string[:half_point]
	last_half = orig_string[half_point:]
	return (first_half, last_half)


def remove_special_characters(orig_string:str) -> str:
	new_str = ''
	for character in orig_string:
		if character in ascii_letters or character in digits or character == ' ':
			new_str += character
	return new_str
