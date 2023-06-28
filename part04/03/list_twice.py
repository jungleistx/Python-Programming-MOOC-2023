# Write your solution here

item_list = []

while True:
	item = int(input("New item: "))

	if item == 0:
		break
	item_list.append(item)
	sorted_list = sorted(item_list)
	print(f"The list now: {item_list}")
	print(f"The list in order: {sorted_list}")

print("Bye!")
