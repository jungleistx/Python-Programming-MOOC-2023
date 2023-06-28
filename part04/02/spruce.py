# Write your solution here
def spruce(height):
    print("a spruce!")
    bottom_row = (height - 1) * 2 + 1
    padding = int(bottom_row / 2)
    i = 0
    spruce = 1
    while i < height:
        print(f"{padding * ' '}{spruce * '*'}")
        spruce += 2
        padding -= 1
        i += 1
    padding = int(bottom_row / 2)
    print(f"{padding * ' '}*")

# You can test your function by calling it within the following block
if __name__ == "__main__":
    spruce(5)
    spruce(3)
    spruce(4)