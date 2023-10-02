# Write your solution here

limit = int(input("Limit: "))

x = 1
total = 0
sum = ""

while total < limit:
    total += x
    sum += str(x)
    x += 1
    if total < limit:
        sum += " + "

print(f"The consecutive sum: {sum} = {total}")