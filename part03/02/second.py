# Write your solution here

string = input("Please type in a string: ")

length = len(string)

if length > 1:
    second = string[1]
    second_to_last = string[-2]

    if second == second_to_last:
        print(f"The second and the second to last characters are {second}")
    else:
        print("The second and the second to last characters are different")