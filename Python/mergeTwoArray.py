def mergeTwoArrayToOne(array1, array2):
    """
    Given two separate lists A and B ordered from least to greatest, construct a list C by:

    repeatedly comparing the least value of A to the least value of B,
    removing (or moving a pointer) the lesser value, and appending it onto C.
    when one list is exhausted, append the remaining items in the other list onto C in order.
    The list C is then also a sorted list.
    Time complexity is O(n)
    :param array1:
    :param array2:
    :return:
    """
    final_array = []
    i = j = 0
    while i < len(array1) and j < len(array2):
        if array1[i] <= array2[j]:
            final_array.append(array1[i])
            i += 1
        else:
            final_array.append(array2[j])
            j += 1

    final_array.extend(array1[i:])
    final_array.extend(array2[j:])
    return final_array


if __name__ == "__main__":
    arr1 = [11, 25, 53, 78, 99]
    arr2 = [19, 22, 36, 66, 110]
    print(mergeTwoArrayToOne(arr1, arr2))
"Output - [11, 19, 22, 25, 36, 53, 66, 78, 99, 110]"
