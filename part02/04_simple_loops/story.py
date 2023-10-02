# Write your solution here

story = ""
last = ""

while True:
    word = input("Please type in a word: ")

    if last == "":
        last = word
    else:
        if last == word:
            break
        else:
            last = word
    if word == "end":
        break
    story += word + " "

print(story)