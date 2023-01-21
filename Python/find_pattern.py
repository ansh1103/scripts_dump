"""
Program to find all the patterns of 0(1+)0 in the given string is discussed here. Given a string containing 0's and 1's, find the total number of 0(1+)0 patterns in the string and output it.
0(1+)0 - There should be at least one '1' between the two 0's.
For example, consider the following string.
Input: 01101111010
Output: 3
Explanation:
01101111010 - count = 1
01101111010 - count = 2
01101111010- count = 3
"""
import re
def find_pattern(string):

    res = re.findall('(0[1]+0)', string)
    print(res)

find_pattern('01101111010')