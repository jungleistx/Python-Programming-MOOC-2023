# Write your solution here
string = input("Please type in a string: ")
sub = input("Please type in a substring: ")
sublength = len(sub)
found = False
spot = 0

while True:
    index = string.find(sub)
    if index < 0:
        found = False
        break
    spot += index
    string = string[index + sublength:]
    if found:
        break
    spot += sublength
    found = True

if found:
    print(f"The second occurrence of the substring is at index {spot}.")
else:
    print("The substring does not occur twice in the string.")