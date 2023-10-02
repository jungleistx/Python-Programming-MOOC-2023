# Write your solution here
word = input("Please type in a word: ")
char = input("Please type in a character: ")

while True:
    if len(word) == 0:
        break
    index = word.find(char)
    if index < 0:
        break
    if index + 3 <= len(word):
        print(word[index:index+3])
        word = word[index + 1:]
    else:
        break
