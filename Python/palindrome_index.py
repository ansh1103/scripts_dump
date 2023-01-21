"""
Given a string of lowercase letters in the range ascii[a-z], determine the index of a character that can be
removed to make the string a palindrome. There may be more than one solution, but any will do. If the word is
 already a palindrome or there is no solution, return -1. Otherwise, return the index of a character to remove.
"""

import math
import os
import random
import re
import sys


# Complete the palindromeIndex function below.
def palindromeIndex(s):
    for i, j in enumerate(range(0, len(s) // 2), 1):
        if s[-i] == s[j]:
            continue
        if s[j:-i] == s[j:-i][::-1]:
            return len(s) - i
        elif s[j + 1:-i + 1] == s[j + 1:-i + 1][::-1]:
            print(s[j + 1:-i + 1])
            print(s[j + 1:-i + 1][::-1])
            return j
        return -1
    return -1


print(palindromeIndex('baa'))
