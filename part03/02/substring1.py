# Write your solution here

string = input("Please type in a string: ")

x = 1

while x <= len(string):
    print(string[:x])
    x += 1