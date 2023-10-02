# Write your solution here
def length(item_list : list) -> int:
    return len(item_list)


# You can test your function by calling it within the following block
if __name__ == "__main__":
    my_list = [3, 6, -4]
    result = length(my_list)
    print(result)
    my_list = [3, 6, -4, 4]
    print(length(my_list))
    my_list = [3, 6, -4, 4, 5, 123, 123, 333, 3, 3, 1]
    print(length(my_list))