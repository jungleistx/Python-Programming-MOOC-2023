# Write your solution here
def same_chars(text, index1, index2):
    length = len(text)
    if length <= index1 or length <= index2:
        return False

    if text[index1] == text[index2]:
        return True
    return False


# You can test your function by calling it within the following block
if __name__ == "__main__":
    print(same_chars("coder", 1, 2))