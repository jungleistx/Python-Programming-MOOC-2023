# Write your solution here
number = int(input("Please type in a number: "))

while number > 0:
    total = 1
    i = 1
    while i <= number:
        total *= i
        i += 1

    print(f"The factorial of the number {number} is {total}")
    number = int(input("Please type in a number: "))

print("Thanks and bye!")