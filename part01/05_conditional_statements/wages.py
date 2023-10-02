# Write your solution here

hourly = float(input("Hourly wage: "))
hours = int(input("Hours worked: "))
day = input("Day of the week: ")

if day == "Sunday":
    wage = hourly * hours * 2
else:
    wage = hourly * hours

print(f"Daily wages: {wage} euros")
