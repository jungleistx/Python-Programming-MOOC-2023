# Write your solution here

number = -1
while number < 0:
	number = int(input("Please type in positive integer: "))

negative = number * -1
for i in range(negative, number + 1):
	if i != 0:
		print(i)