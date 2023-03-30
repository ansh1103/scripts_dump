"""
Returns
- int: the maximum subset sum

Input Format

The first line contains an integer,
.
The second line contains space-separated integers . 
"""
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maxSubsetSum function below.
def maxSubsetSum(arr):
    #Check if arr is empty or contains only 1 elem
    if len(arr) == 0:
        return 0
    if len(arr) == 1:
        return (arr[0] if arr[0] > 0 else 0) 
        
    #initialize the first and second elements in arr for algo
    arr[0] = max(0, arr[0])
    arr[1] = max(arr[0], arr[1])
    
    for i in range(2, len(arr)):
        #Each position is either the previous value,
        #or current value plus one-before the previous
        arr[i] = max(arr[i-1], arr[i] + arr[i-2])
        print("each for loop {}: {}".format(i, arr[i]))
    
    #Return the last value in arr if this value is nonnegative
    if arr[-1] >= 0:
        return arr[-1]
    else:
        return 0
    

if __name__ == '__main__':

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = maxSubsetSum(arr)
    print(res)

