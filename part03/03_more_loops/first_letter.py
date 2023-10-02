# Write your solution here

sentence = input("Please type in a sentence: ")


if len(sentence) > 0:
    print(sentence[0])

index = sentence.find(" ")

while index >= 0:
    print(sentence[index + 1:index + 2])
    sentence = sentence[index + 1:]
    index = sentence.find(" ")