def sumMultiplier(arr):
    """
     function SumMultiplier(arr) take the array of numbers stored in arr and return the string true if any two numbers
      can be multiplied so that the answer is greater than double the sum of all the elements in the array. If not,
       the string false. For example: if arr is [2, 5, 6, -6, 16, 2, 3, 6, 5, 3] then the sum of all these elements is
        and doubling it is 84. There are two elements
     in the array, 16 * 6 = 96 and 96 is greater than 84, so your program should return the string true.
    :param arr:
    :return:
    """
    arraySum = sum(arr)
    for i in range(len(arr)-1):
        for j in range(i+1, len(arr)):
            if arr[i] * arr[j] > 2 * arraySum:
                return True
    return False


if __name__ == '__main__':
    array1 = [2, 5, 6, -6, 16, 2, 3, 6, 5, 3]
    array2 = [2, 2, 2, 2, 4, 1]
    array3 = [1, 1, 2, 10, 3, 1, 12]
    print(f"sumMultiplier(array1)= {sumMultiplier(array1)}")
    print(f"sumMultiplier(array2)= {sumMultiplier(array2)}")
    print(f"sumMultiplier(array3)= {sumMultiplier(array3)}")
