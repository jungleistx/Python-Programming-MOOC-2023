# Write your solution here
number = int(input("Please type in a number: "))

small = 1
big = number
while small <= big:
    if small != big:
        print(small)
        print(big)
    else:
        print(big)
    small += 1
    big -= 1
