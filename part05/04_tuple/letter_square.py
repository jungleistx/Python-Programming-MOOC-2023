# Write your solution here

layers = int(input("Layers: "))

if layers > 26 or layers < 1:
	exit()

size = layers * 2 - 1	# size of the final square
letter = chr(ord('A') + layers - 1) # beginning letter

# top half including middle line
for i in range(0, size // 2 + 1):
	tmp = i

	# first part
	while tmp > 0:
		print(letter, end="")
		letter = chr(ord(letter) - 1)
		tmp -= 1

	# mid part
	multiplier = (ord(letter) - ord('A')) * 2 + 1
	print(f"{letter * multiplier}", end="")

	# end part
	while tmp < i:
		letter = chr(ord(letter) + 1)
		print(letter, end="")
		tmp += 1
	print()


i = size // 2 + 1
# bottom half
while i < size:
	layers -= 1
	tmp = layers
	letter2 = letter

	# first part
	while tmp > 1:
		print(letter2, end="")
		letter2 = chr(ord(letter2) - 1)
		tmp -= 1

	# mid part
	multiplier = (ord(letter2) - ord('A')) * 2 + 1
	print(f"{letter2 * multiplier}", end="")

	# end part
	tmp = 0
	while ord(letter2) < ord(letter):
		letter2 = chr(ord(letter2) + 1)
		print(letter2, end="")
		tmp += 1
	print()

	i += 1

'''
	ord() outputs int from char
	chr() outputs char from int
'''
