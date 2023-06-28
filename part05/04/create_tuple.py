# Write your solution here

def create_tuple(x: int, y: int, z: int) -> tuple:

	smallest = min(x, y, z)
	biggest = max(x, y, z)
	total = x + y + z

	new_tuple = (smallest, biggest, total)
	return new_tuple