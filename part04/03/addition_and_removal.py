# Write your solution here

values = []
counter = 1

while True:
	print(f"The list is now {values}")
	choice = input("a(d)d, (r)emove or e(x)it: ")

	if choice.lower() == 'x':
		break
	elif choice.lower() == 'd':
		values.append(counter)
		counter += 1
	elif choice.lower() == 'r':
		counter -= 1
		if counter < 1:
			break
		values.remove(counter)

print("Bye!")