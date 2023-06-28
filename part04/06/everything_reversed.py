# Write your solution here

def everything_reversed(word_list: list) -> list:

	new_list = []

	for word in word_list:
		new_list.insert(0, f'{word[::-1]}')

	return new_list


if __name__ == "__main__":
	print(everything_reversed(["hi", "there", "hello"]))