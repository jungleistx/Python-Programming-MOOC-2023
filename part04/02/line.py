# Write your solution here
def line(number, text):
    if len(text) > 0:
        print(text[0] * number)
    else:
        print("*" * number)

# You can test your function by calling it within the following block
if __name__ == "__main__":
    line(5, "x")
    line(5, "")
    line(5, "hello")
    line(5, "a")