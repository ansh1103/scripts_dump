def selectionSort(arr):
    """
    The selection sort algorithm sorts an array by repeatedly finding the minimum element (considering ascending order)
     from unsorted part and putting it at the beginning. The algorithm maintains two subarrays in a given array.
    :param arr:
    :return:
    """
    # Traverse through all array elements
    for x in range(len(arr)):
        # Find the minimum element in remaining
        # unsorted array
        minimum_index = x
        for y in range(x+1, len(arr)):
            if arr[minimum_index] > arr[y]:
                minimum_index = y
        # Swap the found minimum element with
        # the first element
        arr[x], arr[minimum_index] = arr[minimum_index], arr[x]
    return arr


if __name__ == "__main__":
    print(selectionSort([64, 25, 12, 22, 11]))
