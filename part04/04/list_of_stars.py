# Write your solution here

def list_of_stars(num_list : list):
	for amount in num_list:
		print(amount * '*')


if __name__ == "__main__":
	list_of_stars([1, 2, 3, 4, 5])
	list_of_stars([1, 5, 3, 4, 5])
