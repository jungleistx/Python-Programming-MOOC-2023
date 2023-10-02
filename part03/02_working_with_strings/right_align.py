# Write your solution here

string = input("Please type in a string: ")

length = len(string)
asterisks = 20 - length

print(f"{'*'*asterisks}{string}")