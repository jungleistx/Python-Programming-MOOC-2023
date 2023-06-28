# Write your solution here
def squared(text, size):
    length = len(text)
    height = 0
    i = 0
    while height < size:
        width = 0
        while width < size:
            print(text[i], end="")
            i += 1
            if i  == length:
                i = 0
            width += 1
        print()
        height += 1

if __name__ == "__main__":
    squared("testing", 4)
    squared("abc", 5)

