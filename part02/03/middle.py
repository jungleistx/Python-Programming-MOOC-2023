# Write your solution here

char1 = input("1st letter: ")
char2 = input("2nd letter: ")
char3 = input("3rd letter: ")

if char1 > char2 and char1 < char3:
    print(f"The letter in the middle is {char1}")
elif char1 > char3 and char1 < char2:
    print(f"The letter in the middle is {char1}")
elif char2 > char1 and char2 < char3:
    print(f"The letter in the middle is {char2}")
elif char2 > char3 and char2 < char1:
    print(f"The letter in the middle is {char2}")
elif char3 > char1 and char3 < char2:
    print(f"The letter in the middle is {char3}")
elif char3 > char2 and char3 < char1:
    print(f"The letter in the middle is {char3}")
