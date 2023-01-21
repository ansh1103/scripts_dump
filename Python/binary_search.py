import time

def time_it(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print("{} took {} milliseconds".format(func.__name__, (end-start) * 1000))
        return result
    return wrapper


@time_it
def binary_search(number_list, number_to_search):
    left_index = 0
    right_index = len(number_list) - 1

    while left_index < right_index:
        mid_index = (left_index + right_index) // 2
        mid_number = number_list[mid_index]

        if mid_number == number_to_search:
            return mid_index

        if mid_number < number_to_search:
            left_index = mid_index + 1
        else:
            right_index = mid_index - 1

    return -1


def binary_search_recursion(number_list, number_to_search, left_index, right_index):
    if right_index < left_index:
        return -1

    mid_index = (left_index + right_index) // 2
    if mid_index >= len(number_list) or mid_index < 0:
        return -1
    mid_number = number_list[mid_index]

    if mid_number == number_to_search:
        return mid_index

    if mid_number < number_to_search:
        left_index = mid_index + 1
    else:
        right_index = mid_index - 1
    return binary_search_recursion(number_list, number_to_search, left_index, right_index)


@time_it
def linear_serach(number_list, number_to_search):
    for i in range(len(number_list) - 1):
        if number_list[i] == number_to_search:
            return i
    return -1


if __name__ == "__main__":
    numberlist = [i for i in range(100, 1000000)]
    # numberlist = [12, 15, 18, 49, 54, 67, 88, 111, 219]
    print(binary_search(numberlist, 999998))

    print(linear_serach(numberlist, 999998))

    print(binary_search_recursion(numberlist, 219, 0, len(numberlist)))