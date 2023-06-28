# Write your solution here

loops = int(input("How many items: "))

i = 1
items = []
while i <= loops:
	number = int(input(f"Item {i}: "))
	items.append(number)
	i += 1

print(items)

