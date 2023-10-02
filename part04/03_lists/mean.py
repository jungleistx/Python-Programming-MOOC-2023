# Write your solution here
def mean(num_list : list) -> float:
    return sum(num_list) / len(num_list)


# You can test your function by calling it within the following block
if __name__ == "__main__":
    my_list = [3, 6, -4]
    result = mean(my_list)
    print(result)
    my_list = [1, 2, 3]
    result = mean(my_list)
    print(result)