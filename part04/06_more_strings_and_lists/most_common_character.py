# Write your solution here

def most_common_character(string: str) -> str:

	occurrence = 0
	most_found = ""

	for char in string:
		if string.count(char) > occurrence:
			most_found = char
			occurrence = string.count(char)

	return most_found