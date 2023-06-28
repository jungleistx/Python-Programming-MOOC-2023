# Write your solution here
def chessboard(size):
    i = 0

    while i < size:

        if i % 2 == 0:
            letter = '1'
        else:
            letter = '0'
        j = 0
        while j < size:
            print(letter, end="")
            j += 1
            if letter == '1':
                letter = '0'
            else:
                letter = '1'

        print()
        i += 1

# Testing the function
if __name__ == "__main__":
    chessboard(3)
    chessboard(4)
    chessboard(6)
