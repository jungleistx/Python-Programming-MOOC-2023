# Write your solution here

print("Person 1:")
person1_name = input("Name: ")
person1_age = int(input("Age: "))
print("Person 2:")
person2_name = input("Name: ")
person2_age = int(input("Age: "))

if person1_age > person2_age:
    print(f"The elder is {person1_name}")
elif person1_age < person2_age:
    print(f"The elder is {person2_name}")
else:
    print(f"{person1_name} and {person2_name} are the same age")