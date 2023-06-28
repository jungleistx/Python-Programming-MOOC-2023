# Write your solution here

def formatted(num_list: list) -> list:

	new_list = []

	for num in num_list:
		new_list.append(f"{num:.2f}")

	return new_list