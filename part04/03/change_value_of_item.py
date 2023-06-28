# Write your solution here

values = [1, 2, 3, 4, 5]

while True:
	index = int(input("Index: "))
	if index == -1:
		break

	newvalue = int(input("New value: "))
	values[index] = newvalue
	print(values)
