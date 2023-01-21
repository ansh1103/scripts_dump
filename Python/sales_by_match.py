"""
There is a large pile of socks that must be paired by color. Given an array of integers representing the color of each sock,
determine how many pairs of socks with matching colors there are.

Example
n = 7
arr =  [1, 2, 1, 2, 1, 3, 2]

There is one pair of color 1 and one of color2 . There are three odd socks left, one of each color. T
The number of pairs is 2
"""
import math
import os
import random
import re
import sys
from collections import Counter


# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    pairs = 0
    unique_element_list = set(ar)
    for element in unique_element_list:
        pairs += ar.count(element) // 2
    return pairs


if __name__ == '__main__':

    result = sockMerchant(7, [1, 2, 1, 2, 1, 3, 2])

    print(result)