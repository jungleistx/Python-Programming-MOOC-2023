# Write your solution here

year = int(input("Year: "))

if year % 4 == 0:
    x = 1
else:
    x = 0

while True:
    if (year + x) % 4 == 0:
        if (year + x) % 100 == 0:
            if (year + x) % 400 == 0:
                print(f"The next leap year after {year} is {year + x}")
                break
        else:
            print(f"The next leap year after {year} is {year + x}")
            break
    x += 1
