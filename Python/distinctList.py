def distinctList(arr):
    """
    Have the function DistinctList(arr) take the array of numbers stored in arr and determine the total number of
    duplicate entries. For example if the input is [1, 2, 2, 2, 3] then your program should output 2 because there are
    two duplicates of one of the elements.
    :param arr:
    :return:
    """
    element_freq_dict = {}
    number_of_dup =0

    for ele in arr:
        if ele not in element_freq_dict.keys():
            element_freq_dict[ele] = 1
        else:
            element_freq_dict[ele] += 1

    for value in element_freq_dict.values():
        if value > 1:
            number_of_dup += value-1

    return number_of_dup


if __name__ == '__main__':
    print(distinctList([1, 2, 2, 2, 3, 3, 4, 3, 3]))
