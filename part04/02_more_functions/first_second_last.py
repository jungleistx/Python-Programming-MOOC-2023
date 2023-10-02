# Write your solution here
def first_word(sentence):

    if len(sentence):
        index = sentence.find(" ")
        if index >= 0:
            return sentence[:index]
        return sentence
    else:
        return ""


def second_word(sentence):

    if len(sentence):
        index = sentence.find(" ")
        if index >= 0:
            sentence = sentence[index + 1:]
            index = sentence.find(" ")
            if index >= 0:
                return sentence[:index]
            else:
                return sentence
        else:
            return ""
    else:
        return ""


def last_word(sentence):

    if len(sentence):
        index = sentence.find(" ")
        while index >= 0:
            sentence = sentence[index + 1:]
            index = sentence.find(" ")
        return sentence
    else:
        return ""


# You can test your function by calling it within the following block
if __name__ == "__main__":
    sentence = "once upon a time there was a programmer"
    print(first_word(sentence))
    print(second_word(sentence))
    print(last_word(sentence))
