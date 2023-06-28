# Write your solution here

word = input("Word: ")

length = len(word)
padding = int((28 - length) / 2)

if length % 2 == 0:
    padding_extra = 0
else:
    padding_extra = 1

print("*"*30)   # top
print(f"*{padding*' '}{word}{padding_extra*' '}{padding * ' '}*")
print("*"*30)   # bottom