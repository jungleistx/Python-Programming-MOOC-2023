# Write your solution here

print("Please type in integer numbers. Type in 0 to finish.")

number = 1
x = 0
sum = 0
positive = 0
negative = 0
while number != 0:
    number = int(input("Number: "))
    if number > 0:
        positive += 1
    elif number < 0:
        negative += 1
    if number != 0:
        x += 1
        sum += number

print(f"Numbers typed in {x}")
print(f"The sum of the numbers is {sum}")
print(f"The mean of the numbers is {sum / x}")
print(f"Positive numbers {positive}")
print(f"Negative numbers {negative}")
