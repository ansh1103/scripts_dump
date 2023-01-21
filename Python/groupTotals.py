def groupTotals(strArr):
    """
    Have the function GroupTotals(strArr) read in the strArr parameter containing key:value pairs where the key
     is a string and the value is an integer. Your program should return a string with new key:value pairs separated
      by a comma such that each key appears only once with the total values summed up.

For example: if strArr is ["B:-1", "A:1", "B:3", "A:5"] then your program should return the string A:6,B:2.

Your final output string should return the keys in alphabetical order. Exclude keys that have a value of 0 after being
summed up
    :param strArr:
    :return:
    """
    result_dict = {}
    for string in strArr:
        k, v = string.split(':')

        if k not in result_dict:
            result_dict[k] = int(v)
        else:
            result_dict[k] += int(v)

    sorted_list = sorted(result_dict.items())
    # print(sorted_d)
    return ','.join([element[0]+':'+str(element[1]) for element in sorted_list if element[1] != 0])


if __name__ == '__main__':
    print(groupTotals(["Z:0", "A:-1"]))


