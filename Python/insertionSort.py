def insertionSort(arr):
    """
    Insertion sort picks one element of a given list at a time and places it at the exact spot where it is to be placed
    :param arr:
    :return:
    """
    for x in range(1, len(arr)):
        key = arr[x]
        j = x-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1

        arr[j+1] = key

    return arr


if __name__ == "__main__":
    print(insertionSort([24, 56, 1, 50, 17]))
