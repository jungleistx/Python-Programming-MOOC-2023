# Write your solution here
def greatest_number(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3


# You can test your function by calling it within the following block
if __name__ == "__main__":
    greatest = greatest_number(5, 4, 8)
    print(greatest)
    greatest = greatest_number(3, 4, 1)
    print(greatest)
    greatest = greatest_number(99, -4, 7)
    print(greatest)
    greatest = greatest_number(0, 0, 0)
    print(greatest)