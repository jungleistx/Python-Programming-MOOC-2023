# Write your solution here

pass_original = input("Password: ")

while True:
    pass_new = input("Repeat password: ")
    if pass_new == pass_original:
        break
    else:
        print("They do not match!")

print("User account created!")