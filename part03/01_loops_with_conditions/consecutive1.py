# Write your solution here

limit = int(input("Limit: "))

x = 1
total = 0

while total < limit:
    total += x
    x += 1

print(total)