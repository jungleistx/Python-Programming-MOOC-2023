# Copy here code of line function from previous exercise and use it in your solution
def line(number, text):
    if len(text) > 0:
        print(text[0] * number)
    else:
        print("*" * number)


def shape(width, tri_char, height, rec_char):

    i = 1
    while i <= width:
        line(i, tri_char)
        i += 1

    i = 0
    while i < height:
        line(width, rec_char)
        i += 1


# You can test your function by calling it within the following block
if __name__ == "__main__":
    shape(5, "x", 2, "o")