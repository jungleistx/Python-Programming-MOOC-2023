# Write your solution here

def longest(strings: list) -> str:

	current_longest = len(strings[0])
	pos = -1
	for i in range(len(strings)):
		if len(strings[i]) > current_longest:
			current_longest = len(strings[i])
			pos = i

	return strings[pos]


if __name__ == "__main__":
	strings = ["hi", "hiya", "hello", "howdydoody", "hi there"]
	print(longest(strings))