def consecutive(arr):
    """
    Have the function Consecutive(arr) take the array of integers stored in arr and return the minimum number of
    integers needed to make the contents of arr consecutive from the lowest number to the highest number.
    For example: If arr contains [4, 8, 6] then the output should be 2 because two numbers need to be added to the
    array (5 and 7) to make it a consecutive array of numbers from 4 to 8. Negative numbers may be entered as
     parameters and no array will have less than 2 elements.
    :param arr:
    :return:
    """
    if len(arr) < 2:
        return 0
    else:
        sorted_arr = list(sorted(arr))
        numbers = []
        for i in range(sorted_arr[0]+1, max(sorted_arr)):
            if i not in sorted_arr:
                numbers.append(i)
        return len(numbers)


if __name__ == '__main__':
    print(consecutive([4, 8, 15, 6]))
