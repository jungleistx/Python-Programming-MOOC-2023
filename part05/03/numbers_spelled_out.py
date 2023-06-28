# Write your solution here

def dict_of_numbers() -> dict:
	new_dict = {}

	singles = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']

	tens = ['', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']

	for i in range(0, 20):
		new_dict[i] = singles[i]

	for i in range(20, 100):
		index = i // 10
		if i % 10 == 0:
			new_dict[i] = tens[index]
		else:
			first_number = tens[index]
			last_number = singles[i % 10]
			new_dict[i] = f"{first_number}-{last_number}"

	return new_dict