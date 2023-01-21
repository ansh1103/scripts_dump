def print_pairs(arr, N):
    """a program to check and return the pairs of a given array A whose sum value is equal to a target value N."""
    hash_set = set()
    for i in range(len(arr)):
        val = N - arr[i]
        if val in hash_set:
            print("Pairs found - {}, {}".format(arr[i], str(val)))
            
        hash_set.add(arr[i])

arr = [1,2,423,3,6,8]
N = 9
print_pairs(arr, N)