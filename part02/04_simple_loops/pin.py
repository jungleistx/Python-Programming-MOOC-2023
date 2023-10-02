# Write your solution here

guess = 0

while True:
    pin = int(input("PIN: "))
    guess += 1

    if pin == 4321:
        break
    else:
        print("Wrong")

if guess == 1:
    print("Correct! It only took you one single attempt!")
else:
    print(f"Correct! It took you {guess} attempts")